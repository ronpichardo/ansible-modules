#!/usr/bin/python

#!/usr/bin/python

from ansible.module_utils.basic import *

def main():

    module = AnsibleModule(argument_spec={})

    response = { "update": "outdated" }
    module.exit_json(changed=False, data=response)


if __name__ == '__main__':
    main()
