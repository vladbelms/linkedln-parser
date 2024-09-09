import sys
from typing import Optional, Callable, List
import blessed
from .element import Element


class Option(Element):
    def __init__(self,
                 name: str,
                 handler: Callable,
                 description: Optional[str] = "",
                 deleting_handler: Optional[Callable] = None
                 ):
        super().__init__(name,
                         handler,
                         description
                         )
        self.deleting_handler = deleting_handler

    def display(self, selected: bool) -> str:
        option_text = f"{self.name} | {self.description}" if self.description else self.name
        return f"> {option_text}" if selected else f"  {option_text}"

    def activate(self):
        super().activate()

    def __repr__(self):
        return f"Option(name ={self.name}, description={self.description})"

