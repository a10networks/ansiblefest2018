#!/usr/bin/python

# Eric Chou (ericc@a10networks.com, Twitter @ericchou)

DOCUMENTATION = """
---
"""

EXAMPLES = """
"""

def main():

    import requests, json
    from requests.packages.urllib3.exceptions import InsecureRequestWarning
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

    # AnsibleModule API from ansible.module_utils.basic
    # for ingesting Playbook inventory parameters
    module = AnsibleModule(
        argument_spec = dict(
            host = dict(required=True),
            username = dict(required=True),
            password = dict(required=True),
            commands = dict(type='list', required=True)
        )
    )
    a10_device = module.params.get('host')
    base_url = 'https://'+ a10_device
    username = module.params.get('username')
    password = module.params.get('password')
    commands = module.params.get('commands')

    # Acquire athorization token
    auth_headers = {'content-type': 'application/json'}
    auth_payload = {"credentials": {"username": username, "password": password}}
    auth_endpoint = '/axapi/v3/auth'
    url = base_url + auth_endpoint
    r = requests.post(url, data=json.dumps(auth_payload), headers=auth_headers, verify=False)
    signature =  r.json()['authresponse']['signature']

    # Headers beyond this point should include the authorization token
    common_headers = {'Content-type' : 'application/json', 'Authorization' : 'A10 {}'.format(signature)}

    # cli_deploy
    cli_deploy_endpoint = '/axapi/v3/clideploy'
    url = base_url + cli_deploy_endpoint
    cli_deploy_payload = {
        "commandList": list(commands)
    }
    result = requests.post(url, data=json.dumps(cli_deploy_payload), headers=common_headers, verify=False)
    data = json.dumps({
        "Result": result.content
    })

    # Log off
    logoff_endpoing = '/axapi/v3/logoff'
    url = base_url + logoff_endpoing
    #print("Log off")
    r = requests.post(url, headers=common_headers, verify=False)

    # Signals module exit
    module.exit_json(changed=False, msg=str(data))

# Ansible standard for import at the bottom instead of top
from ansible.module_utils.basic import *
main()

