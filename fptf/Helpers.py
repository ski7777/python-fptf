#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#


from .AttributeBadTypeException import AttributeBadTypeException


def getOptionalValue(data, key, valtype):
    if key not in data:
        # return None if key not in data
        return(None)
    if type(data[key]) != valtype:
        # raise Error if value not type valtype
        raise AttributeBadTypeException(key, valtype)
    # return value
    return(data[key])


def setDictValueNotNone(data, key, value):
    if value != None:
        # set value if not None
        data[key] = value
    # return new dict
    return(data)
