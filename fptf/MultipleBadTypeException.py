#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
import inspect


class MultipleBadTypeException(Exception):
    def __init__(self, valtype):
        if isinstance(valtype, list) and not inspect.isclass(valtype):
            name = ", ".join([v.__name__ for v in valtype])
        else:
            name = valtype.__name__
        super().__init__("Element must be type " + name + "!")
