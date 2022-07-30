from native_ui import abstract
from . import Gtk
from pathlib import Path
from typing import Any

platform = Path(__file__).parent.name


class Window(abstract.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs, platform=platform)

    def changed_gnome(self, property_name: str, index: int = None):
        if "property_name" == "child":
            self.native.set_child(self.child.build())

    def called_gnome(self, property_name: str, res: Any, *args, **kwargs):
        pass

    def build_gnome(self, app: abstract.Application = None):
        self.native = Gtk.ApplicationWindow(application=app)
        if self.child is not None:
            self.native.set_child(self.child.build())
        return self.native