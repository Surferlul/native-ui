from native_ui import abstract
from . import Adw
from pathlib import Path
from typing import Any
from .. import gnome

platform = Path(__file__).parent.name


class Application(abstract.Application):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs, platform=platform)

    def changed_gnome(self, property_name: str, index: int = None):
        pass

    def called_gnome(self, property_name: str, res: Any, *args, **kwargs):
        pass

    def build_gnome(self):
        class GnomeApp(Adw.Application):
            def __init__(self, **kwargs):
                super().__init__(**kwargs)
                self.connect('activate', self.on_activate)
                self.abstract_window = None
                self.window = None

            def on_activate(self, app):
                if self.window is None:
                    if self.abstract_window is not None:
                        self.window = self.abstract_window.build(app)
                    else:
                        return
                self.window.present()

        self.native = GnomeApp(application_id=gnome.application_id)
        if self.window is not None:
            self.native.abstract_window = self.window
        return self.native

    def run_gnome(self, *args, **kwargs):
        self.native.run(*args, **kwargs)
