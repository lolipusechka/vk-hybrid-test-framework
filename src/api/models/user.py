import json


class User(object):
    def __init__(self, data: str or int):
        if type(data) == str:
            self.__dict__ = json.loads(data)
            self.__id = self.__dict__.get("id")
        elif type(data) == int:
            self.__id = data
        else:
            raise ValueError("Class Photo init only with str and int")

    @property
    def id(self):
        return self.__id

    def __str__(self) -> str:
        return f"User.id = {self.__id}"


