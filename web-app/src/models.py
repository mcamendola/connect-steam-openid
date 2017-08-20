import json

class User(object):

    def __init__(self, id, nickname):
        self.__id = id
        self.__nickname = nickname

    @property
    def id(self):
        return self.__id

    @property
    def nickname(self):
        return self.__nickname