from native_ui import abstract
from . import Gtk
from pathlib import Path
from typing import Any

platform = Path(__file__).parent.name


class Window(abstract.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs, platform=platform)

    def changed_gnome(self, property_name: str, index: int = None):
        match property_name:
            case "child": self.set_child_gnome()
            case "title": self.set_title_gnome()
            case "width": self.set_width_gnome()
            case "height": self.set_height_gnome()

    def called_gnome(self, property_name: str, res: Any, *args, **kwargs):
        pass

    def set_title_gnome(self):
        if self.title is not None:
            self.native.set_title(self.title)

    def set_width_gnome(self):
        if self.width is not None:
            self.native.set_default_size(self.width,
                                         self.native.get_default_size()[1])

    def set_height_gnome(self):
        if self.height is not None:
            self.native.set_default_size(self.native.get_default_size()[0],
                                         self.height)

    def set_child_gnome(self):
        if self.child is not None:
            self.native.set_child(self.child.build())

    def build_gnome(self, app: abstract.Application = None):
        self.native = Gtk.ApplicationWindow(application=app)
        self.set_child_gnome()
        self.set_title_gnome()
        self.set_width_gnome()
        self.set_height_gnome()
        return self.native