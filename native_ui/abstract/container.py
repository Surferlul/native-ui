from . import Abstract, Layout, abstract_property


class Container(Abstract):
    def __init__(self, layout: Layout = Layout.HORIZONTAL, children: list = None, platform: str = None):
        super().__init__(platform=platform)
        if children is None:
            children = []
        self._children = children
        self._layout = layout

    @abstract_property
    def layout(self, value):
        self._layout = value

    def get_children(self):
        return self._children

    def add_child(self, child):
        self._children.append(child)

    def pop_child(self, index):
        return self._children.pop(index)
