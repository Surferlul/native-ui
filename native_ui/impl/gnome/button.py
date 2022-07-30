from native_ui import abstract
from . import Gtk
from pathlib import Path
from typing import Any

platform = Path(__file__).parent.name


class Button(abstract.Button):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs, platform=platform)

    def changed_gnome(self, property_name: str, index: int = None):
        pass

    def called_gnome(self, property_name: str, res: Any, *args, **kwargs):
        pass

    def clicked(self, _native_button):
        self.call("press", self)

    def build_gnome(self):
        self.native = Gtk.Button(label=self.label)
        self.native.connect('clicked', self.clicked)
        return self.native