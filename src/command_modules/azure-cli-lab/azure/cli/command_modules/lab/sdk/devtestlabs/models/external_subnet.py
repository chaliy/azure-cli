# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# coding: utf-8
# pylint: skip-file
from msrest.serialization import Model


class ExternalSubnet(Model):
    """ExternalSubnet.

    :param id: Gets or sets the identifier.
    :type id: str
    :param name: Gets or sets the name.
    :type name: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
    }

    def __init__(self, id=None, name=None):
        self.id = id
        self.name = name
