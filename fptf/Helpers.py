#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#


from .AttributeBadTypeException import AttributeBadTypeException
from. AttributeMissingException import AttributeMissingException


def getValue(data, key, valtype, required):
    #check whether key in data
    if key not in data:
        if required:
            # raise error if not present and required
            raise AttributeMissingException(key)
        else:
            # return None if not present but not required
            return(None)
    if type(data[key]) != valtype:
        # raise Error if value not type valtype
        raise AttributeBadTypeException(key, valtype)
    # return value
    return(data[key])


def getValueOptional(data, key, valtype):
    return(getValue(data, key, valtype, False))


def getValueRequired(data, key, valtype):
    return(getValue(data, key, valtype, True))


def setDictValueNotNone(data, key, value):
    if value != None:
        # set value if not None
        data[key] = value
    # return new dict
    return(data)
