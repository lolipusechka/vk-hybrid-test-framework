import json


class Post(object):
    def __init__(self, json_str: str):
        self.__dict__ = json.loads(json_str)
        self.__id = self.__dict__.get("response").get("post_id")

    @property
    def id(self):
        return self.__id
