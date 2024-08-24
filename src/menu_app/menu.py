import sys
from typing import Optional, Callable, List
import blessed


class Option:
    def __init__(self,
                 name: str,
                 handler: Callable,
                 description: Optional[str] = "",
                 deleting_handler: Optional[Callable] = None
                 ):
        self.name = name
        self.handler = handler
        self.description = description
        self.deleting_handler = deleting_handler

    def __repr__(self):
        return f"Option(name ={self.name}, description={self.description})"


class KeyMode:

    def __init__(
            self,
            options: list[Option],
            description: str,
            term: blessed.Terminal = blessed.Terminal()
    ) -> None:

        self.__description = description
        self.__options = options
        self.__term = term

    @property
    def description(self) -> str:
        return self.__description

    @property
    def options(self) -> list[str]:
        return self.__options

    def __call__(self):
        term = self.__term
        options = self.options

        exit_option = Option(
            name='Exit',
            description='Exit the program',
            handler=sys.exit
        )

        options.append(exit_option)

        current_option = 0
        padded_name_len = max([len(option.name) for option in options]) + 2

        use_description = any(option.description for option in options)
        padded_description_len = max([len(option.description) for option in options], default=0) + 2 if use_description else None

        with term.fullscreen(), term.cbreak(), term.hidden_cursor():
            while True:
                print(term.move_yx(0, 0) + term.clear())

                if self.description:
                    print(term.bold_green(self.description + '\n'))

                for i, option in enumerate(options):
                    name = option.name.ljust(padded_name_len)

                    if use_description and option.description:
                        description = option.description.ljust(padded_description_len)
                        option_text = f'{name} | {description}'
                    else:
                        option_text = name

                    if i == current_option:
                        print(term.green_reverse(f"> {option_text}"))
                    else:
                        print(f"  {option_text}")

                key = term.inkey()

                last_option_idx = len(options) - 1
                if key.name == 'KEY_UP':
                    current_option = (current_option - 1) % len(options)
                elif key.name == 'KEY_DOWN':
                    current_option = (current_option + 1) % len(options)
                elif key == '\n' or key.name == 'KEY_ENTER':
                    selected_option = options[current_option]
                    selected_option.handler()
                    break
                elif key == '\n' or key.name == 'KEY_ENTER':
                    selected_option = options[current_option]
                    break

        return selected_option.handler()

    @staticmethod
    def screen_option(
            label: str,
            description: Optional[str],
            options: List[Option],
            deleting_handler: Optional[Callable] = None
    ) -> Option:
        def _handler():
            keymode = KeyMode(options, description)
            keymode()

        return Option(
            name=label,
            handler=_handler,
            description=description,
            deleting_handler=deleting_handler
        )


class NumberAdjuster:
    def __init__(self, start_number: int, term: blessed.Terminal = blessed.Terminal()):
        self.number = start_number
        self.term = term

    def adjust(self):
        with self.term.fullscreen(), self.term.cbreak(), self.term.hidden_cursor():
            while True:
                print(self.term.move_yx(0, 0) + self.term.clear())
                print(f"Current number: {self.number}")
                print("Press UP to increase, DOWN to decrease, ENTER to confirm, ESC to exit.")

                key = self.term.inkey()

                if key.name == 'KEY_UP':
                    self.number += 1
                elif key.name == 'KEY_DOWN':
                    self.number -= 1
                elif key == '\n' or key.name == 'KEY_ENTER':
                    return self.number
                elif key.name == 'KEY_ESCAPE':
                    break


class ListSelector:
    def __init__(self, items: List[str], term: blessed.Terminal = blessed.Terminal()):
        self.items = items
        self.current_index = 0
        self.term = term

    def select(self):
        with self.term.fullscreen(), self.term.cbreak(), self.term.hidden_cursor():
            while True:
                print(self.term.move_yx(0, 0) + self.term.clear())
                print("Choose an option:")

                for i, item in enumerate(self.items):
                    if i == self.current_index:
                        print(self.term.green_reverse(f"> {item}"))
                    else:
                        print(f"  {item}")

                print("\nPress UP/DOWN to choose, ENTER to select, ESC to exit.")

                key = self.term.inkey()

                if key.name == 'KEY_UP':
                    self.current_index = (self.current_index - 1) % len(self.items)
                elif key.name == 'KEY_DOWN':
                    self.current_index = (self.current_index + 1) % len(self.items)
                elif key == '\n' or key.name == 'KEY_ENTER':
                    return self.items[self.current_index]
                elif key.name == 'KEY_ESCAPE':
                    break
