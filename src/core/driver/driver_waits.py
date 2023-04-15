from selenium.webdriver.support.wait import WebDriverWait

from src.core.driver.driver import Driver
from src.utils.json_parser import get_config

config = get_config("general.json")


def explicit_wait():
    return WebDriverWait(Driver.get_instance(), timeout=int(config["time_out_in_seconds"]))
