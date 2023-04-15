import logging as log
import pytest

from src.core.driver.driver import Driver
from src.utils.json_parser import get_config

config = get_config("general.json")


class BaseTest:

    @pytest.fixture()
    def setup(self):
        try:
            log.getLogger().info(f"Test initialize with '{config['browser']}'")
            Driver.get_instance()
            yield "setup"
            log.getLogger().info(f"The web driver {Driver} is stopping...")
            Driver.set_instance_none_and_quit()
            log.getLogger().info(f"The web driver {Driver} was stopped")
        finally:
            Driver.set_instance_none_and_quit()
