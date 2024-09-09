import sys
from typing import Optional, Callable, List
import blessed
from .element import Element


class Slider(Element):
    def __init__(self,
                 start_number: int,
                 handler: Callable,
                 term: blessed.Terminal = blessed.Terminal()
                 ):
        super().__init__(name="Slider",
                         handler=handler,
                         description=""
                         )
        self.number = start_number
        self.term = term

    def display(self, selected: bool) -> str:
        slider_text = f"Slider: {self.number}"
        return f"> {slider_text}" if selected else f"  {slider_text}"

    def activate(self):
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
                    if self.handler:
                        self.handler(self.number)
                    return self.number
                elif key.name == 'KEY_ESCAPE':
                    break
