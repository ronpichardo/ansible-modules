# My Custom Ansible Modules

## Overview
TODO(Not yet implemented)
Ansible supplies many pre-built modules, but non work using them against Crestron hardware.  Developing two modules:
1. crestron_copy = will allow me to copy files to a filepath provided 
2. crestron_update = will allow me to check for a new firmware, and if one is found, it will load the new firmware file to prep for upgrade
3. crestron_upgrade = will upgrade crestron devices if a file with a newer firmware is loaded

## Requirements
Ansible is required, as it is the tool that will be used for automation

## Findings
using `transport=paramiko` in the ansible.cfg file, helps with running the raw module on crestron devices.
the example-playbook.yml helps to atleast connect with the raw and send a debug message to the console with the result of the command passed in the playbook
