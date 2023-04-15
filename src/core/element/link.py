from src.core.base.base_element import BaseElement


class Link(BaseElement):
    def __init__(self, by, locator, name):
        super().__init__(by, locator, name)
