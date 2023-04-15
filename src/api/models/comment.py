import json


class Comment(object):
    def __init__(self, json_str: str):
        self.__dict__ = json.loads(json_str)
        self.__id = self.__dict__.get("response").get("comment_id")

    @property
    def id(self):
        return self.__id
