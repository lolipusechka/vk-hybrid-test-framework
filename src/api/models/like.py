import json
from typing import List

from src.api.models.user import User


class Like(object):
    def __init__(self, json_str: str):
        self.__dict__ = json.loads(json_str)
        self.__count = self.__dict__.get("response").get("count")
        self.__users_id = self.__dict__. get("response").get("users")
        self.__users = []
        for item in self.__users_id:
            self.__users.append(User(item["uid"]))

    @property
    def count(self):
        return self.__count

    @property
    def users(self) -> List[User]:
        return self.__users
