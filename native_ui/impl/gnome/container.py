from native_ui import abstract
from . import Gtk
from pathlib import Path
from typing import Any

platform = Path(__file__).parent.name


class Container(abstract.Container):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs, platform=platform)

    def changed_gnome(self, property_name: str, index: int = None):
        match property_name:
            case "layout": self.set_layout_gnome()
            case "children": self.set_children_gnome()

    def called_gnome(self, property_name: str, res: Any, *args, **kwargs):
        match property_name:
            case "add_child": self.native.append(args[0].build())
            case "pop_child": self.native.remove(res.native)

    def set_layout_gnome(self):
        if self.layout is not None:
            match self.layout:
                case abstract.Layout.HORIZONTAL: self.native.set_orientation(Gtk.Orientation.HORIZONTAL)
                case abstract.Layout.VERTICAL: self.native.set_orientation(Gtk.Orientation.VERTICAL)

    def set_children_gnome(self):
        for child in self.children:
            self.native.append(child.build())


    def build_gnome(self):
        self.native = Gtk.Box()
        self.set_layout_gnome()
        self.set_children_gnome()
        return self.native