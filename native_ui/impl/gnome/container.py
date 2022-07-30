from native_ui import abstract
from . import Gtk
from pathlib import Path
from typing import Any

platform = Path(__file__).parent.name


class Container(abstract.Container):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs, platform=platform)

    def changed_gnome(self, property_name: str, index: int = None):
        pass

    def called_gnome(self, property_name: str, res: Any, *args, **kwargs):
        if property_name == "add_child":
            self.native.append(args[0].build())

    def build_gnome(self):
        orientation = Gtk.Orientation.VERTICAL
        if self.layout == abstract.Layout.HORIZONTAL:
            orientation = Gtk.Orientation.HORIZONTAL
        self.native = Gtk.Box(orientation=orientation)
        for child in self.call("get_children"):
            self.native.append(child.build())
        return self.native