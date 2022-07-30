from . import Abstract, abstract_property


class Window(Abstract):
    def __init__(self, child: Abstract = None, platform: str = None):
        super().__init__(platform=platform)
        self._child = child

    @abstract_property
    def child(self, value):
        self._child = value
