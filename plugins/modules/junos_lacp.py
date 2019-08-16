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
The module file for junos_lacp
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
module: junos_lacp
version_added: 2.9
short_description: Manage Global Link Aggregation Control Protocol (LACP) on Juniper Junos devices
description: This module provides declarative management of global LACP on Juniper Junos network devices.
author: Ganesh Nalawade (@ganeshrn)
options:
  config:
    description: A dictionary of LACP global options
    type: dict
    suboptions:
      system_priority:
        description:
        - LACP priority for the system.
        type: int
      link_protection:
        description:
        - Enable LACP link-protection for the system. If the value is set to C(non-revertive)
          it will not revert links when a better priority link comes up. By default the link will
          be reverted.
        type: str
        choices: ['revertive', 'non-revertive']
  state:
    description:
    - The state the configuration should be left in
    type: str
    choices:
    - merged
    - replaced
    - deleted
    default: merged
requirements:
  - ncclient (>=v0.6.4)
notes:
  - This module requires the netconf system service be enabled on
    the remote device being managed.
  - Tested against vSRX JUNOS version 18.1R1.
  - This module works with connection C(netconf). See L(the Junos OS Platform Options,../network/user_guide/platform_junos.html).
"""
EXAMPLES = """
# Using deleted

# Before state:
# -------------
# user@junos01# show chassis aggregated-devices ethernet lacp
# system-priority 63;
# link-protection {
#    non-revertive;
# }

- name: Delete global LACP attributes
  junos_lacp:
    state: deleted

# After state:
# ------------
# user@junos01# show chassis aggregated-devices ethernet lacp
#


# Using merged

# Before state:
# -------------
# user@junos01# show chassis aggregated-devices ethernet lacp
#

- name: Merge global LACP attributes
  junos_lacp:
    config:
      system_priority: 63
      link_protection: revertive
    state: merged

# After state:
# ------------
# user@junos01# show chassis aggregated-devices ethernet lacp
# system-priority 63;
# link-protection {
#    non-revertive;
# }


# Using replaced

# Before state:
# -------------
# user@junos01# show chassis aggregated-devices ethernet lacp
# system-priority 63;
# link-protection {
#    non-revertive;
# }

- name: Replace global LACP attributes
  junos_lacp:
    config:
      system_priority: 30
      link_protection: non-revertive
    state: replaced

# After state:
# ------------
# user@junos01# show chassis aggregated-devices ethernet lacp
# system-priority 30;
# link-protection;


"""
RETURN = """
before:
  description: The configuration prior to the model invocation.
  returned: always
  type: dict
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
after:
  description: The resulting configuration model invocation.
  returned: when changed
  type: dict
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
xml:
  description: The set of xml rpc payload pushed to the remote device.
  returned: always
  type: list
  sample: ['xml 1', 'xml 2', 'xml 3']
"""


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.juniper.junos.plugins.module_utils.network.junos.argspec.lacp.lacp import (
    LacpArgs,
)
from ansible_collections.juniper.junos.plugins.module_utils.network.junos.config.lacp.lacp import (
    Lacp,
)


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    module = AnsibleModule(
        argument_spec=LacpArgs.argument_spec, supports_check_mode=True
    )

    result = Lacp(module).execute_module()
    module.exit_json(**result)


if __name__ == "__main__":
    main()