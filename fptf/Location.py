#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#

from .Helpers import getOptionalValue, setDictValueNotNone


class Location:
    _name = None
    _address = None
    _longitude = None
    _latitude = None
    _altitude = None

    def __init__(self, data={}):
        if type(data) != dict:
            # raise error if data is not type dict
            raise TypeError("Data must be type dict")
        # check whether data is not empty
        if data != {}:
            if not "type" in data:
                # raise error when type attribute not present
                raise AttributeMissingException("type")
            if data["type"] != "location":
                # raise error when type attribute not is present
                raise ValueError("Type must be \"location\"")
            # parse items
            self._name = getOptionalValue(data, "name", str)
            self._address = getOptionalValue(data, "address", str)
            self._longitude = getOptionalValue(data, "longitude", float)
            self._latitude = getOptionalValue(data, "latitude", float)
            self._altitude = getOptionalValue(data, "altitude", float)
            if (self._longitude != None) != (self._latitude != None):
                # raise error if only one of longitude and latitude is present
                raise ValueError("You must supply both longitude and latitude or none of them!")

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
        self._name = None

    @property
    def address(self):
        # getter for address
        return(self._address)

    @address.setter
    def address(self, value):
        # setter for address
        if type(value) != str:
            # raise error if address not type string
            raise TypeError("Address must be type str!")
        self._address = value

    @address.deleter
    def address(self):
        # deleter for address
        self._address = None

    @property
    def coordinate(self):
        # getter for coordinate
        return((self._longitude, self._latitude))

    @coordinate.setter
    def coordinate(self, value):
        # setter for coordinate
        if type(value) != tuple:
            # raise error if coordinate not type tuple
            raise TypeError("coordinate must be type tuple!")
        # extract values
        lon, lat = value
        if type(lon) != float:
            # raise error if longitude not type float
            raise TypeError("Longitude must be type float!")
        if type(lat) != float:
            # raise error if latitude not type float
            raise TypeError("Latitude must be type float!")
        self._longitude = lon
        self._latitude = lat

    @coordinate.deleter
    def coordinate(self):
        # deleter for coordinate
        self._longitude = None
        self._latitude = None

    @property
    def altitude(self):
        # getter for altitude
        return(self._altitude)

    @altitude.setter
    def altitude(self, value):
        # setter for altitude
        if type(value) != float:
            # raise error if altitude not type float
            raise TypeError("Altitude must be type float!")
        self._altitude = value

    @altitude.deleter
    def altitude(self):
        # deleter for altitude
        self._altitude = None

    def toFPTF(self):
        # create empty dict
        fptf = {}
        # copy values to dict if present
        fptf = setDictValueNotNone(fptf, "name", self._name)
        fptf = setDictValueNotNone(fptf, "address", self._address)
        fptf = setDictValueNotNone(fptf, "longitude", self._longitude)
        fptf = setDictValueNotNone(fptf, "latitude", self._latitude)
        fptf = setDictValueNotNone(fptf, "altitude", self._altitude)
        # return dict
        return(fptf)
