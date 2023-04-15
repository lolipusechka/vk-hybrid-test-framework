import json


class Photo(object):
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
