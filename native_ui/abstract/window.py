from . import Abstract, abstract_property


class Window(Abstract):
    def __init__(self,
                 child: Abstract = None,
                 title: str = None,
                 width: int = None,
                 height: int = None,
                 platform: str = None):
        super().__init__(platform=platform)
        self._child = child
        self._title = title
        self._width = width
        self._height = height

    @abstract_property
    def child(self, value):
        self._child = value

    @abstract_property
    def title(self, value):
        self._title = value

    @abstract_property
    def width(self, value):
        self._width = value

    @abstract_property
    def height(self, value):
        self._height = value
