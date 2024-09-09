from typing import Optional, Callable


class Element:
    def __init__(self,
                 name: str,
                 handler: Callable,
                 description: Optional[str] = ""
                 ) -> None:
        self.name = name
        self.handler = handler
        self.description = description

    def display(self, selected: bool) -> str:
        raise NotImplementedError

    def activate(self):
        if self.handler:
            self.handler()

