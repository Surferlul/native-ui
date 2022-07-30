import native_ui
from typing import Callable, Any
from collections import defaultdict
from enum import Enum


class Layout(Enum):
    HORIZONTAL = 0
    VERTICAL = 1


def abstract_property(function: Callable):
    def fget(self):
        return getattr(self, f"_{function.__name__}")

    def fset(self, value):
        function(self, value)
        self.changed(function.__name__)

    return property(fget, fset)


class Abstract(object):
    def __init__(self, platform: str = None):
        self.is_builder = False
        if not hasattr(self, "supported_platforms"):
            self.supported_platforms = set()
        if platform is not None:
            self.supported_platforms.add(platform)
        self.native = None

    def set(self, **kwargs):
        for prop in kwargs:
            self.set_property(prop, kwargs[prop])

    def set_property(self, property_name: str, value: Any, index: int = None):
        if index is None:
            setattr(self, property_name, value)
        else:
            getattr(self, property_name)[index] = value
        self.changed(property_name, index=index)

    def call(self, property_name: str, *args, **kwargs):
        res = getattr(self, property_name)(*args, **kwargs)
        self.called(property_name, res, *args, **kwargs)
        return res

    def native_call(self, property_name: str, *args, **kwargs):
        if native_ui.runtime_platform is None:
            print("No runtime platform set")
        if native_ui.runtime_platform not in self.supported_platforms:
            print(f"Platform {native_ui.runtime_platform} not supported by {type(self).__name__}")
        else:
            return getattr(self, f"{property_name}_{native_ui.runtime_platform}")(*args, **kwargs)

    def changed(self, property_name: str, index: int = None):
        if self.native is not None:
            self.native_call("changed", property_name, index)

    def called(self, property_name: str, res: Any, *args, **kwargs):
        if self.native is not None:
            self.native_call("called", property_name, res, *args, **kwargs)

    def build(self, *args, **kwargs):
        if self.native is not None:
            return self.native
        return self.native_call("build", *args, **kwargs)

    class __metaclass__(type):
        __inheritors__ = defaultdict(list)

        def __new__(meta, name, bases, dct):
            klass = type.__new__(meta, name, bases, dct)
            for base in klass.mro()[1:-1]:
                meta.__inheritors__[base].append(klass)
            return klass


from .button import Button
from .container import Container
from .window import Window
from .application import Application
