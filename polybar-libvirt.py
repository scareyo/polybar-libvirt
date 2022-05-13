#!/usr/bin/env python3

#
# polybar-libvirt - get the status of a virtual machine
#

import sys
import libvirt

# Configuration
stateStr = [
    "n/a",              # (0) VIR_DOMAIN_NOSTATE
    "running",          # (1) VIR_DOMAIN_RUNNING
    "blocked",          # (2) VIR_DOMAIN_BLOCKED
    "paused",           # (3) VIR_DOMAIN_PAUSED
    "shutting down",    # (4) VIR_DOMAIN_SHUTDOWN
    "shut off",         # (5) VIR_DOMAIN_SHUTOFF
    "crashed",          # (6) VIR_DOMAIN_CRASHED
    "suspended"         # (7) VIR_DOMAIN_PMSUSPENDED
]

def main():
    if len(sys.argv) < 2:
        print("usage: polybar-libvirt [vmname]")
        sys.exit(1)

    vmName = sys.argv[1]
    state = get_state(vmName)

    print(stateStr[state])

def get_state(vmName):
    try:
        conn = libvirt.openReadOnly("qemu:///system")
    except libvirt.libvirtError:
        sys.exit(1)

    try:
        domain = conn.lookupByName(vmName)
    except libvirt.libvirtError:
        sys.exit(1)

    return domain.info()[0]


if __name__ == "__main__":
    main()
