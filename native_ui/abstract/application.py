from . import Abstract, abstract_property, Window


class Application(Abstract):
    def __init__(self, window: Window = None, platform: str = None):
        super().__init__(platform=platform)
        self._window = window

    @abstract_property
    def window(self, value):
        self._window = value

    def run(self, *args, **kwargs):
        self.native_call("run", *args, **kwargs)
