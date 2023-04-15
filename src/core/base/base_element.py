import logging as log
from selenium.webdriver.support import expected_conditions as EC

from src.core.driver.driver_find_element import *
from src.core.driver.driver_waits import explicit_wait
from src.utils.action_utils import pause


class BaseElement:

    def __init__(self, by: str, locator: str, name: str):
        self.by = by
        self.locator = locator
        self.name = name

    def click_element(self):
        log.getLogger().info(f"Click on the element '{self.name}'")
        explicit_wait().until(lambda d: d.find_element(self.by, self.locator)).click()

    def is_visible(self):
        pause()
        log.getLogger().info(f"Check the visibility of element '{self.name}'")
        b = find_element(self.by, self.locator).is_displayed()
        log.getLogger().info(f"Element '{self.name}' is {('not visible','visible')[b]}")
        return b

    def wait_for_displayed(self):
        log.getLogger().info(f"Wait for visibility of element '{self.name}'")
        explicit_wait().until(EC.visibility_of_element_located((self.by, self.locator)))

    def wait_for_not_displayed(self):
        log.getLogger().info(f"Wait for not visibility of element '{self.name}'")
        explicit_wait().until(EC.invisibility_of_element(self.get_web_element()))

    def wait_for_clickable(self):
        log.getLogger().info(f"Wait for clickable of element '{self.name}'")
        explicit_wait().until(EC.element_to_be_clickable((self.by, self.locator)))

    def get_text(self):
        log.getLogger().info(f"Get text from the element '{self.name}'")
        return explicit_wait().until(lambda d: d.find_element(self.by, self.locator)).text

    def get_text_from_attribute(self, attribute):
        log.getLogger().info(f"Get text by attribute '{attribute}' from the element '{self.name}'")
        return explicit_wait().until(lambda d: d.find_element(self.by, self.locator)).get_attribute(attribute)

    def get_web_element(self):
        return explicit_wait().until(lambda d: d.find_element(self.by, self.locator))
