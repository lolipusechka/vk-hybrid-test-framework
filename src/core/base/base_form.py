import logging as log

from src.core.base.base_element import BaseElement


class BaseForm:
    def __init__(self, unique_element: BaseElement, name: str):
        self.__unique_element = unique_element
        self.__name = name

    def is_displayed(self) -> bool:
        log.getLogger().info(f"Check the visibility of the page '{self.__name}'")
        return self.__unique_element.is_visible()
