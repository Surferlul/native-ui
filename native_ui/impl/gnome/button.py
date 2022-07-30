from native_ui import abstract
from . import Gtk
from pathlib import Path
from typing import Any

platform = Path(__file__).parent.name


class Button(abstract.Button):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs, platform=platform)

    def changed_gnome(self, property_name: str, index: int = None):
        match property_name:
            case "label": self.set_label_gnome()

    def called_gnome(self, property_name: str, res: Any, *args, **kwargs):
        pass

    def set_label_gnome(self):
        if self.label is not None:
            self.native.set_label(self.label)

    def clicked(self, _native_button):
        self.call("press")

    def build_gnome(self):
        self.native = Gtk.Button()
        self.native.connect('clicked', self.clicked)
        self.set_label_gnome()
        return self.native