#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#


class AttributeBadTypeException(Exception):
    def __init__(self, attribute, valtype):
        super().__init__("Attribute \"" + attribute + "\" must be type " + valtype.__name__ + "!")
