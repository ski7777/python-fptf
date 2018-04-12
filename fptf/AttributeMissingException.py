#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#


class AttributeMissingException(Exception):
    def __init__(self, attribute):
        super().__init__("Attribute \"" + attribute + "\" is missing!")
