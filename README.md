# polybar-libvirt
A polybar script for retreiving the status of a VM from libvirt

## Configuration
Status strings can be configured inside the script
```
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
```

## Example
```
[module/win11]
type = custom/script
tail = true
exec = ~/bin/polybar-libvirt.py win11
label =  %output%
```
