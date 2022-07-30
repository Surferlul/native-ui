from . import Abstract, abstract_property
from typing import Callable


class Button(Abstract):
    def __init__(self,
                 label: str = None,
                 pressed: Callable = lambda *args, **kwargs: None,
                 pressed_args: list = None,
                 pressed_kwargs: dict = None,
                 platform: str = None):
        super().__init__(platform=platform)
        self._label = label
        self._pressed = pressed
        if pressed_args is None:
            pressed_args = []
        if pressed_kwargs is None:
            pressed_kwargs = {}
        self.pressed_args = pressed_args
        self.pressed_kwargs = pressed_kwargs

    @abstract_property
    def label(self, value):
        self._label = value

    @abstract_property
    def pressed(self, value):
        self._pressed = value

    def press(self, *args, **kwargs):
        self.call("pressed", self, *args, *self.pressed_args, **kwargs, **self.pressed_kwargs)
