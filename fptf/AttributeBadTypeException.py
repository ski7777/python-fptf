#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
import inspect


class AttributeBadTypeException(Exception):
    def __init__(self, attribute, valtype):
        if isinstance(valtype, list) and not inspect.isclass(valtype):
            name = ", ".join([v.__name__ for v in valtype])
        else:
            name = valtype.__name__
        super().__init__("Attribute \"" + attribute + "\" must be type " + name + "!")
