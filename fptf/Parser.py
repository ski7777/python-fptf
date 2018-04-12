#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#

from .AttributeMissingException import AttributeMissingException
from .Location import Location


def parseFPTF(data):
    # determine type of data
    if type(data) == dict:
        # single object -> parse directly
        return(parseItem(data))
    elif type(data) == list:
        # list -> parse one by one
        items = []
        # iterate over list
        for item in data:
            # parse object
            items.append(parseItem(item))
        return(items)
    # raise error if unsupported type
    raise TypeError("Data format does not match dict or list!")


def parseItem(data):
    if type(data) != dict:
        raise TypeError("Data must be type dict!")
    if not "type" in data:
        # raise error when type attribute not present
        raise AttributeMissingException("type")
    # determine type of data
    if data["type"] == "location":
        return(Location(data))
    elif data["type"] == "station":
        pass
    elif data["type"] == "stop":
        pass
    elif data["type"] == "region":
        pass
    elif data["type"] == "line":
        pass
    elif data["type"] == "route":
        pass
    elif data["type"] == "schedule":
        pass
    elif data["type"] == "journey":
        pass
    # raise error if type is unknown
    raise ValueError(data["type"] + " does not match any known type!")


def toFPTF(data):
    # define known FPTF classes:
    classes = [Location]
    # check whether data is FPTF class
    if type(data) in classes:
        # call class' toFPTF function
        return(data.toFPTF())
    elif type(data) == list:
        # list -> convert one by one
        items = []
        # iterate over list
        for item in data:
            if type(item) not in classes:
                # raise error if type of item is not FPTF class
                raise TypeError("Item is not subclass of class FPTF")
            # call item's toFPTF function and append to list
            items.append(item.toFPTF())