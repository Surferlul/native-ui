import gi

gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw

application_id = None


def requirements(app_id: str):
    global application_id
    application_id = app_id


from .button import Button
from .container import Container
from .window import Window
from .application import Application
