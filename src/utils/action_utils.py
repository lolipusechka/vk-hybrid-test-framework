from selenium.webdriver.common.action_chains import ActionChains

from src.core.driver.driver import Driver
from src.utils.json_parser import get_config

__config = get_config("general.json")


def pause():
    actions = ActionChains(Driver.get_instance())
    actions.pause(int(__config["pause_in_seconds"]))
    actions.perform()

