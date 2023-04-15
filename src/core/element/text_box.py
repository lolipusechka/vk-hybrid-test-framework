import logging as log

from src.core.base.base_element import BaseElement


class Textbox(BaseElement):
    def __init__(self, by, locator, name):
        super().__init__(by, locator, name)

    def send_text(self, text: str):
        log.getLogger().info(f"Enter '{text}' in textbox '{self.name}'")
        super().get_web_element().send_keys(text)

    def clear_text(self):
        log.getLogger().info(f"Clear textbox '{self.name}'")
        super().get_web_element().clear()
