import sys
from blessed import Terminal


class Menu:

    def __init__(self, title: str, options: list[str], settings: dict = None, setting_handlers: dict = None) -> None:
        self.__title = title
        self.__options = options
        self.__term = Terminal()
        self.__should_exit = False
        self.__settings = settings or {}
        self.__setting_handlers = setting_handlers or {}
        self.__current_option = 0

    @property
    def title(self) -> str:
        return self.__title

    @property
    def options(self) -> list[str]:
        return self.__options

    @property
    def term(self):
        return self.__term

    @property
    def should_exit(self):
        return self.__should_exit

    @property
    def settings(self):
        return self.__settings

    @property
    def setting_handlers(self):
        return self.__setting_handlers

    def show_list(self, list_: list[dict], title: str = 'List') -> None:
        start_index = 0
        end_index = min(len(list_), self.__term.height - 4)

        with self.__term.cbreak(), self.__term.hidden_cursor():
            while True:
                print(self.__term.clear())
                print(self.__term.move_y(2))
                print(self.__term.move_x(2) + title)

                for i in range(start_index, end_index):
                    dictionary = list_[i]
                    for key, value in dictionary.items():
                        print(f"{key}: {value}")
                    print(self.__term.horizontal_line(self.__term.width))

                print(self.__term.move_y(self.__term.height - 2))
                print(self.__term.center('Press ENTER to return'))

                val = self.__term.inkey()

                if val.name == 'KEY_UP' and start_index > 0:
                    start_index -= 1
                    end_index -= 1
                elif val.name == 'KEY_DOWN' and end_index < len(list_):
                    start_index += 1
                    end_index += 1
                elif val.name == 'KEY_ENTER':
                    break

    def settings_menu(self) -> None:
        item_keys = list(self.__settings.keys())
        current_setting_index = 0

        with self.__term.fullscreen(), self.__term.cbreak(), self.__term.hidden_cursor():
            while True:
                print(self.__term.clear())
                print(self.__term.move_y(self.__term.height // 2 - 2))
                print(self.__term.center('Settings Menu'))

                for i, key in enumerate(item_keys):
                    value = self.__settings[key]
                    if i == current_setting_index:
                        print(self.__term.move_y(self.__term.height // 2 - 1 + i))
                        print(self.__term.center(self.__term.on_blue(self.__term.bold(f'{key}: {value}'))))
                    else:
                        print(self.__term.move_y(self.__term.height // 2 - 1 + i))
                        print(self.__term.center(f'{key}: {value}'))

                print(self.__term.move_y(self.__term.height // 2 + len(item_keys)))
                print(self.__term.center(
                    'Press UP/DOWN to navigate, LEFT/RIGHT to modify, ENTER to save and return'))

                val = self.__term.inkey()

                if val.name == 'KEY_UP':
                    current_setting_index = (current_setting_index - 1) % len(item_keys)
                elif val.name == 'KEY_DOWN':
                    current_setting_index = (current_setting_index + 1) % len(item_keys)
                elif val.name == 'KEY_LEFT' or val.name == 'KEY_RIGHT':
                    key = item_keys[current_setting_index]
                    handler = self.__setting_handlers.get(key)
                    if handler:
                        self.__settings[key] = handler(self.__settings[key], val.name)
                elif val.name == 'KEY_ENTER':
                    break

    def display_menu(self) -> None:
        with self.__term.fullscreen(), self.__term.cbreak(), self.__term.hidden_cursor():
            while True:
                print(self.__term.clear())
                print(self.__term.move_y(2))
                print(self.__term.move_x(2) + self.__title)
                for i, option in enumerate(self.__options):
                    print(self.__term.move_y(4 + i))
                    if i == self.__current_option:
                        print(self.__term.move_x(2) + self.__term.on_blue(self.__term.bold(f'> {option} ')))
                    else:
                        print(self.__term.move_x(2) + f'  {option} ')

                val = self.__term.inkey()

                if val.name == 'KEY_UP':
                    self.__current_option = (self.__current_option - 1) % len(self.__options)
                elif val.name == 'KEY_DOWN':
                    self.__current_option = (self.__current_option + 1) % len(self.__options)
                elif val.name == 'KEY_ENTER':
                    return self.__current_option

    def run(self) -> None:
        while not self.__should_exit:
            selected_option = self.display_menu()
            if selected_option == len(self.__options) - 1:
                self.__should_exit = True
            elif selected_option == 1:
                self.settings_menu()
