import sys
from typing import Optional, Callable, List
import blessed
from .elements import Element, Option


class KeyMode:

    def __init__(
            self,
            elements: list[Element],
            description: str,
            term: blessed.Terminal = blessed.Terminal()
    ) -> None:

        self.__description = description
        self.__elements = elements
        self.__term = term

    @property
    def description(self) -> str:
        return self.__description

    @property
    def elements(self) -> list[Element]:
        return self.__elements

    def __call__(self):
        term = self.__term
        elements = self.elements

        exit_option = Option(
            name='Exit',
            description='Exit the program',
            handler=sys.exit
        )

        elements.append(exit_option)

        current_option = 0
        padded_name_len = max([len(element.name) for element in elements]) + 2

        use_description = any(element.description for element in elements)
        padded_description_len = max([len(element.description) for element in elements], default=0) + 2 if use_description else None

        with term.fullscreen(), term.cbreak(), term.hidden_cursor():
            while True:
                print(term.move_yx(0, 0) + term.clear())

                if self.description:
                    print(term.bold_green(self.description + '\n'))

                for i, element in enumerate(elements):
                    name = element.name.ljust(padded_name_len)

                    if use_description and element.description:
                        description = element.description.ljust(padded_description_len)
                        option_text = f'{name} | {description}'
                    else:
                        option_text = name

                    if i == current_option:
                        print(term.green_reverse(f"> {option_text}"))
                    else:
                        print(f"  {option_text}")

                key = term.inkey()

                if key.name == 'KEY_UP':
                    current_option = (current_option - 1) % len(elements)
                elif key.name == 'KEY_DOWN':
                    current_option = (current_option + 1) % len(elements)
                elif key == '\n' or key.name == 'KEY_ENTER':
                    selected_option = elements[current_option]
                    selected_option.handler()
                    break
                elif key == '\n' or key.name == 'KEY_ENTER':
                    selected_option = elements[current_option]
                    break

        return selected_option.handler()

    @staticmethod
    def screen_option(
            label: str,
            description: str,
            elements: List[Element],
            deleting_handler: Optional[Callable] = None
    ) -> Option:
        def _handler():
            keymode = KeyMode(elements, description)
            keymode()

        return Option(
            name=label,
            handler=_handler,
            description=description,
            deleting_handler=deleting_handler
        )
