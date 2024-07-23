import sys
from blessed import Terminal


class Menu:

    def __init__(self):
        self.__region = 'USA'
        self.__vacancies = 5
        self.__term = Terminal()
        self.__should_exit = False

    @property
    def region(self):
        return self.__region

    @property
    def vacancies(self):
        return self.__vacancies

    @property
    def term(self):
        return self.__term

    @property
    def should_exit(self):
        return self.__should_exit

    def show_list(self, list_: list) -> None:
        start_index = 0
        end_index = min(len(list_), self.__term.height - 4)

        with self.__term.cbreak(), self.__term.hidden_cursor():
            while True:
                print(self.__term.clear())
                print(self.__term.move_y(2))
                print(self.__term.move_x(2) + 'Vacancies List')

                for i in range(start_index, end_index):
                    dictionary = list_[i]
                    for key, value in dictionary.items():
                        print(f"{key}: {value}")
                    print(self.__term.horizontal_line(self.__term.width))

                print(self.__term.move_y(self.__term.height - 2))
                print(self.__term.center('Press UP/DOWN to scroll, ENTER to return'))

                val = self.__term.inkey()

                if val.name == 'KEY_UP' and start_index > 0:
                    start_index -= 1
                    end_index -= 1
                elif val.name == 'KEY_DOWN' and end_index < len(list_):
                    start_index += 1
                    end_index += 1
                elif val.name == 'KEY_ENTER':
                    break

    def settings(self):
        regions = ['UK', 'USA', 'EU']
        region_index = regions.index(self.__region)

        while True:
            print(self.__term.clear())
            print(self.__term.move_y(self.__term.height // 2 - 2))
            print(self.__term.center('Settings Menu'))
            print(self.__term.move_y(self.__term.height // 2 - 1))
            print(self.__term.center(f'Region: {regions[region_index]}'))
            print(self.__term.move_y(self.__term.height // 2))
            print(self.__term.center(f'Vacancies: {self.__vacancies}'))
            print(self.__term.move_y(self.__term.height // 2 + 2))
            print(self.__term.center(
                'Press UP/DOWN to change region, LEFT/RIGHT to change vacancies, ENTER to save and return'))

            val = self.__term.inkey()

            if val.name == 'KEY_UP':
                region_index = (region_index - 1) % len(regions)
            elif val.name == 'KEY_DOWN':
                region_index = (region_index + 1) % len(regions)
            elif val.name == 'KEY_LEFT':
                self.__vacancies = max(1, self.__vacancies - 1)
            elif val.name == 'KEY_RIGHT':
                self.__vacancies += 1
            elif val.name == 'KEY_ENTER':
                self.__region = regions[region_index]
                break

    def display_menu(self) -> None:
        current_option = 0
        options = ['Parse', 'Settings', 'Exit']

        with self.__term.fullscreen(), self.__term.cbreak(), self.__term.hidden_cursor():
            while True:
                print(self.__term.clear())
                print(self.__term.move_y(2))
                print(self.__term.move_x(2) + 'Linkedin Parser')
                for i, option in enumerate(options):
                    print(self.__term.move_y(4 + i))
                    if i == current_option:
                        print(self.__term.move_x(2) + self.__term.on_blue(self.__term.bold(f'> {option} ')))
                    else:
                        print(self.__term.move_x(2) + f'  {option} ')

                val = self.__term.inkey()

                if val.name == 'KEY_UP':
                    current_option = (current_option - 1) % len(options)
                elif val.name == 'KEY_DOWN':
                    current_option = (current_option + 1) % len(options)
                elif val.name == 'KEY_ENTER':
                    if current_option == 0:
                        return
                    elif current_option == 1:
                        self.settings()
                    elif current_option == 2:
                        self.__should_exit = True
                        print(self.__term.clear())
                        return
