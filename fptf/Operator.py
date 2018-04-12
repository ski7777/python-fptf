#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#

from .Helpers import getValueRequired, setDictValueNotNone


class Operator:
    _id = None
    _name = None

    def __init__(self, data={}, id=None, name=None):
        if type(data) != dict:
            # raise error if data is not type dict
            raise TypeError("Data must be type dict")
        # check whether data is not empty
        if data != {}:
            if not "type" in data:
                # raise error when type attribute not present
                raise AttributeMissingException("type")
            if data["type"] != "operator":
                # raise error when type attribute not is present
                raise ValueError("Type must be \"operator\"")
            # parse items
            self._id = getValueRequired(data, "id", str)
            self._name = getValueRequired(data, "name", str)
        # check whether id is present
        if id != None:
            if type(id) != str:
                # raise error if id not type string
                raise TypeError("Id must be type str!")
            self._id = id
        # check name id is present
        if name != None:
            if type(name) != str:
                # raise name if id not type string
                raise TypeError("Name must be type str!")
            self._name = name

    @property
    def id(self):
        # getter for id
        return(self._id)

    @id.setter
    def id(self, value):
        # setter for id
        if type(value) != str:
            # raise error if id not type string
            raise TypeError("Id must be type str!")
        self._id = value

    @id.deleter
    def id(self):
        # deleter for id
        # id cannot be deleted
        raise PermissionError("id cannot be deleted!")

    @property
    def name(self):
        # getter for name
        return(self._name)

    @name.setter
    def name(self, value):
        # setter for name
        if type(value) != str:
            # raise error if name not type string
            raise TypeError("Name must be type str!")
        self._name = value

    @name.deleter
    def name(self):
        # deleter for name
        # name cannot be deleted
        raise PermissionError("Name cannot be deleted!")

    def toFPTF(self):
        # create empty dict
        fptf = {}
        # copy values to dict
        fptf["id"] = self._id
        fptf["name"] = self._name
        # return dict
        return(fptf)