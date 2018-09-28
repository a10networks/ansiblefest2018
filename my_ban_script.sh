#!/usr/bin/env bash
#
# export banned ip into enviornmental vairable to be read in playbook
# there is a bug in module for entering the same ip in the class-map
#

export ban_ip="$1"

if [ "$4" = "ban" ]; then
    echo "ban"
    echo "ip $1 direction $2 pps $3 action $4"
    ansible-playbook -i hosts flowspec_playbook.yml
    exit 0
fi

