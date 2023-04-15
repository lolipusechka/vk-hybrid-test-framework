import os
from pathlib import Path


def find(name):
    for root, dirs, files in os.walk(__get_project_root()):
        if name in files:
            return os.path.join(root, name)


def __get_project_root() -> str:
    return os.path.abspath(Path(__file__).parents[3])
