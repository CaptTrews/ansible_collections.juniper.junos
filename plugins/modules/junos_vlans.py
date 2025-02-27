#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2019 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

#############################################
#                WARNING                    #
#############################################
#
# This file is auto generated by the resource
#   module builder playbook.
#
# Do not edit this file manually.
#
# Changes to this file will be over written
#   by the resource module builder.
#
# Changes should be made in the model used to
#   generate this file or in the resource module
#   builder template.
#
#############################################

"""
The module file for junos_vlans
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type

ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "network",
}

DOCUMENTATION = """
---
module: junos_vlans
version_added: 2.9
short_description: Create and manage VLAN configurations on Junos OS
description: This module creates and manages VLAN configurations on Junos OS.
author: Daniel Mellado (@danielmellado)
requirements:
  - ncclient (>=v0.6.4)
notes:
  - This module requires the netconf system service be enabled on
    the remote device being managed
  - Tested against Junos OS 18.4R1
  - This module works with connection C(netconf). See L(the Junos OS
    Platform Options,../network/user_guide/platform_junos.html).
options:
  config:
    description: A dictionary of Vlan options
    type: list
    elements: dict
    suboptions:
      vlan_id:
        description:
          - IEEE 802.1q VLAN identifier for VLAN (1..4094).
        type: int
        required: true
      name:
        description:
          - Name of VLAN.
        type: str
        required: true
      description:
        description:
          - Text description of VLANs
        type: str
  state:
    description:
      - The state the configuration should be left in.
    type: str
    choices:
      - merged
      - replaced
      - overridden
      - deleted
    default: merged
"""

EXAMPLES = """
# Using merged
#############

# Before State
# ------------
#
# admin# show vlans
# vlan-2 {
#     vlan-id 2;
# }
# vlan-3 {
#     vlan-id 3;
# }

- name: Merge JUNOS vlan
  junos_vlans:
    config:
      - name: vlan-1
        vlan-id: 1
  state: merged

# After State
# -----------
#
# admin# show vlans
# vlan-1 {
#     vlan-id 1;
# }
# vlan-2 {
#     vlan-id 2;
# }
# vlan-3 {
#     vlan-id 3;
# }


# Using replaced
################

# Before State
# ------------
#
# admin# show vlans
# vlan-1 {
#     vlan-id 1;
# }
# vlan-2 {
#     vlan-id 2;
# }
# vlan-3 {
#     vlan-id 3;
# }

- name: Replace JUNOS vlan
  junos_vlans:
    config:
      - name: vlan-1
        vlan-id: 10
      - name: vlan-3
        vlan-id: 30
  state: replaced

# After State
# -----------
#
# admin# show vlans
# vlan-1 {
#     vlan-id 10;
# }
# vlan-2 {
#     vlan-id 2;
# }
# vlan-3 {
#     vlan-id 30;
# }


# Using overridden
##################

# Before State
# ------------
#
# admin# show vlans
# vlan-1 {
#     vlan-id 1;
# }
# vlan-2 {
#     vlan-id 2;
# }
# vlan-3 {
#     vlan-id 3;
# }

- name: Override JUNOS vlan
  junos_vlans:
    config:
      - name: vlan-4
        vlan-id: 100
      - name: vlan-2
        vlan-id: 200
  state: overridden

# After State
# -----------
#
# admin# show vlans
# vlan-2 {
#     vlan-id 200;
# }
# vlan-4 {
#     vlan-id 100;
# }


#Using deleted
##############

# Before State
# ------------
#
# admin# show vlans
# vlan-1 {
#     vlan-id 1;
# }
# vlan-2 {
#     vlan-id 2;
# }
# vlan-3 {
#     vlan-id 3;
# }

- name: Delete JUNOS vlan
  junos_vlans:
    config:
      - name: vlan-1
  state: deleted

# After State
# -----------
#
# admin# show vlans
# vlan-2 {
#     vlan-id 2;
# }
# vlan-3 {
#     vlan-id 3;
# }
"""

RETURN = """
before:
  description: The configuration prior to the model invocation.
  returned: always
  type: str
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
after:
  description: The resulting configuration model invocation.
  returned: when changed
  type: str
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
commands:
  description: The set of commands pushed to the remote device.
  returned: always
  type: list
  sample: ['xml 1', 'xml 2', 'xml 3']
"""


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.juniper.junos.plugins.module_utils.network.junos.argspec.vlans.vlans import (
    VlansArgs,
)
from ansible_collections.juniper.junos.plugins.module_utils.network.junos.config.vlans.vlans import (
    Vlans,
)


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    module = AnsibleModule(
        argument_spec=VlansArgs.argument_spec, supports_check_mode=True
    )

    result = Vlans(module).execute_module()
    module.exit_json(**result)


if __name__ == "__main__":
    main()
