# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# coding: utf-8
# pylint: skip-file
from msrest.serialization import Model


class Port(Model):
    """Port.

    :param transport_protocol: Protocol type of the port. Possible values
     include: 'Tcp', 'Udp'
    :type transport_protocol: str or :class:`TransportProtocol
     <azure.mgmt.devtestlabs.models.TransportProtocol>`
    :param backend_port: Backend port of the target virtual machine.
    :type backend_port: int
    """

    _attribute_map = {
        'transport_protocol': {'key': 'transportProtocol', 'type': 'str'},
        'backend_port': {'key': 'backendPort', 'type': 'int'},
    }

    def __init__(self, transport_protocol=None, backend_port=None):
        self.transport_protocol = transport_protocol
        self.backend_port = backend_port
