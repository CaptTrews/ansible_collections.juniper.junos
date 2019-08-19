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
The module file for junos_lag_interfaces
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
module: junos_lag_interfaces
version_added: 2.9
short_description: Manage Link Aggregation on Juniper JUNOS devices.
description: This module manages properties of Link Aggregation Group on Juniper JUNOS devices.
author: Ganesh Nalawade (@ganeshrn)
options:
  config:
    description: A list of link aggregation group configurations.
    type: list
    suboptions:
      name:
        description:
        - Name of the link aggregation group (LAG).
        type: str
        required: True
      mode:
        description:
          - LAG mode. A value of C(passive) will enable LACP in C(passive) mode that is it
            will respond to LACP packets and C(active) configures the link to initiate
            transmission of LACP packets.
        choices: ['active', 'passive']
      link_protection:
        description:
          - This boolean option indicates if link protection should be enabled for the LAG interface.
            If value is C(True) link protection is enabled on LAG and if value is C(False) link protection
            is disabled.
        type: bool
      members:
        description:
          - List of member interfaces of the link aggregation group. The value can be
            single interface or list of interfaces.
        type: list
        suboptions:
          member:
            description:
              - Name of the member interface.
            type: str
          link_type:
            description:
              - The value of this options configures the member link as either C(primary)
                or C(backup). Value C(primary) configures primary interface for link-protection mode
                and C(backup) configures backup interface for link-protection mode.
            choices: ['primary', 'backup']
  state:
    description:
    - The state the configuration should be left in
    type: str
    choices:
    - merged
    - replaced
    - overridden
    - deleted
    default: merged
requirements:
  - ncclient (>=v0.6.4)
notes:
  - This module requires the netconf system service be enabled on
    the remote device being managed.
  - Tested against vSRX JUNOS version 18.4R1.
  - This module works with connection C(netconf). See L(the Junos OS Platform Options,../network/user_guide/platform_junos.html).
"""
EXAMPLES = """
# Using merged

# Before state:
# -------------
# user@junos01# show interfaces
# ge-0/0/1 {
#    description "Ansible configured interface 1";
#    ether-options {
#        802.3ad ae0;
#    }
# }
# ge-0/0/2 {
#    description "Ansible configured interface 2";
#    ether-options {
#        802.3ad ae0;
#    }
# }
# ae0 {
#     description "lag interface";
# }
# ae1 {
#     description "lag interface 1";
# }

- name: "Delete LAG attributes of given interfaces (Note: This won't delete the interface itself)"
  junos_lag_interfaces:
    config:
      - name: ae0
      - name: ae1
    state: deleted

# After state:
# -------------
# user@junos01# show interfaces
# ge-0/0/1 {
#    description "Ansible configured interface 1";
# }
# ge-0/0/2 {
#    description "Ansible configured interface 2";
# }


# Using merged

# Before state:
# -------------
# user@junos01# show interfaces
# ge-0/0/1 {
#    description "Ansible configured interface 1";
# }
# ge-0/0/2 {
#    description "Ansible configured interface 2";
# }

- name: Merge provided configuration with device configuration
  junos_lag_interfaces:
    config:
      - name: ae0
        members:
          - member: ge-0/0/1
            link_type: primary
          - member: ge-0/0/2
            link_type: backup
    state: merged

# After state:
# -------------
# user@junos01# show interfaces
# ge-0/0/1 {
#    description "Ansible configured interface 1";
#    ether-options {
#        802.3ad {
#            ae0;
#            primary;
#        }
#    }
# }
# ge-0/0/2 {
#    description "Ansible configured interface 2";
#    ether-options {
#        802.3ad {
#            ae0;
#            backup;
#        }
#    }
# }


# Using merged

# Before state:
# -------------
# user@junos01# show interfaces
# ge-0/0/1 {
#    description "Ansible configured interface 1";
#    ether-options {
#        802.3ad ae0;
#    }
# }
# ge-0/0/2 {
#    description "Ansible configured interface 2";
#    ether-options {
#        802.3ad ae0;
#    }
# }
# ae0 {
#     description "lag interface";
# }
# ae3 {
#     description "lag interface 3";
# }

- name: Overrides all device LAG configuration with provided configuration
  junos_lag_interfaces:
    config:
      - name: ae0
        members:
          - member: ge-0/0/2
      - name: ae1
        members:
          - member: ge-0/0/1
        mode: passive
    state: overridden

# After state:
# -------------
# user@junos01# show interfaces
# ge-0/0/1 {
#    description "Ansible configured interface 1";
#    ether-options {
#        802.3ad ae1;
#    }
# }
# ge-0/0/2 {
#    description "Ansible configured interface 2";
#    ether-options {
#        802.3ad ae0;
#    }
# }
# ae0 {
#     description "lag interface";
# }
# ae1 {
#    aggregated-ether-options {
#        lacp {
#            active;
#        }
#    }
# }


# Using merged

# Before state:
# -------------
# user@junos01# show interfaces
# ge-0/0/1 {
#    description "Ansible configured interface 1";
# }
# ge-0/0/2 {
#    description "Ansible configured interface 2";
# }
# ge-0/0/3 {
#    description "Ansible configured interface 3";
# }

- name: Replace device LAG configuration with provided configuration
  junos_lag_interfaces:
    config:
      - name: ae0
        members:
          - member: ge-0/0/1
        mode: active
    state: replaced

# After state:
# -------------
# user@junos01# show interfaces
# ge-0/0/1 {
#    description "Ansible configured interface 1";
#    ether-options {
#        802.3ad ae0;
#    }
# }
# ge-0/0/2 {
#    description "Ansible configured interface 2";
# }
# ae0 {
#    aggregated-ether-options {
#        lacp {
#            active;
#        }
#    }
# }
# ge-0/0/3 {
#    description "Ansible configured interface 3";
# }


"""
RETURN = """
before:
  description: The configuration prior to the model invocation.
  returned: always
  type: list
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
after:
  description: The resulting configuration model invocation.
  returned: when changed
  type: list
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
from ansible_collections.juniper.junos.plugins.module_utils.network.junos.argspec.lag_interfaces.lag_interfaces import (
    Lag_interfacesArgs,
)
from ansible_collections.juniper.junos.plugins.module_utils.network.junos.config.lag_interfaces.lag_interfaces import (
    Lag_interfaces,
)


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    module = AnsibleModule(
        argument_spec=Lag_interfacesArgs.argument_spec,
        supports_check_mode=True,
    )

    result = Lag_interfaces(module).execute_module()
    module.exit_json(**result)


if __name__ == "__main__":
    main()
