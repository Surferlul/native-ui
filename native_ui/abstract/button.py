from . import Abstract, abstract_property
from typing import Callable


class Button(Abstract):
    def __init__(self,
                 label: str = "",
                 pressed: Callable = lambda button: None,
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
        self._pressed_args = pressed_args
        self._pressed_kwargs = pressed_kwargs

    @abstract_property
    def label(self, value):
        self._label = value

    @abstract_property
    def pressed(self, value):
        self._pressed = value

    @abstract_property
    def pressed_args(self, value):
        self._pressed_args = value

    def add_pressed_arg(self, value):
        self._pressed_args.append(value)

    @abstract_property
    def pressed_kwargs(self, value):
        self._pressed_kwargs = value

    def set_pressed_kwarg(self, key, value):
        self._pressed_kwargs[key] = value

    def press(self, *args, **kwargs):
        self.call("pressed", *args, *self._pressed_args, **kwargs, **self._pressed_kwargs)
