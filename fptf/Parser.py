#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#

from .AttributeMissingException import AttributeMissingException
from .Location import Location
from .Operator import Operator


def parseFPTF(data):
    # determine type of data
    if isinstance(data, dict):
        # single object -> parse directly
        return(parseItem(data))
    elif isinstance(data, list):
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
    if not isinstance(data, dict):
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
    elif data["type"] == "operator":
        return(Operator(data))
    elif data["type"] == "journey":
        pass
    # raise error if type is unknown
    raise ValueError(data["type"] + " does not match any known type!")


def toFPTF(data):
    # define known FPTF classes:
    classes = [Location, Operator]
    # check whether data is FPTF class
    if type(data) in classes:
        # call class' toFPTF function
        return(data.toFPTF())
    elif isinstance(value, list):
        # list -> convert one by one
        items = []
        # iterate over list
        for item in data:
            if type(item) not in classes:
                # raise error if type of item is not FPTF class
                raise TypeError("Item is not FPTF class!")
            # call item's toFPTF function and append to list
            items.append(item.toFPTF())
        return(items)
    # raise error if item is not FPTF class
    raise TypeError("Item is not FPTF class!")
