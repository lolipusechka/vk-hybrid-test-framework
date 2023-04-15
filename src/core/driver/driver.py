from src.core.browser.browser_factory import Factory
from src.utils.json_parser import get_config

config = get_config("general.json")


class Driver:
    __driver = None

    @staticmethod
    def get_instance():
        if not Driver.__driver:
            Driver.__driver = Factory.get_browser().create_driver()
            return Driver.__driver
        else:
            return Driver.__driver

    @staticmethod
    def set_instance_none_and_quit():
        if not Driver.__driver:
            pass
        else:
            Driver.__driver.quit()
            Driver.__driver = None
