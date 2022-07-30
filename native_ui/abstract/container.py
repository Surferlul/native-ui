from . import Abstract, Layout, abstract_property, abstract_method


class Container(Abstract):
    def __init__(self, layout: Layout = None, children: list = None, platform: str = None):
        super().__init__(platform=platform)
        if children is None:
            children = []
        self._children = children
        self._layout = layout

    @abstract_property
    def layout(self, value):
        self._layout = value

    @abstract_property
    def children(self, value):
        # in case for loop manipulates value through reference
        value = [child for child in value]
        for _ in range(len(self._children)):
            self.pop_child(0)
        self._children = value

    @abstract_method
    def add_child(self, child):
        self._children.append(child)

    @abstract_method
    def pop_child(self, index):
        return self._children.pop(index)
