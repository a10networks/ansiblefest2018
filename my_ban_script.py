eference. https://github.com/pavel-odintsov/fastnetmon/blob/master/src/scripts/fastnetmon_notify.py
#
import sys
from sys import stdin
import optparse
import logging, json

# This script will get following params:
#  $1 client_ip_as_string
#  $2 data_direction
#  $3 pps_as_string
#  $4 action (ban or unban)

LOG_FILE = "/var/log/fastnetmon-notify.log"


logger = logging.getLogger("DaemonLog")
logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler = logging.FileHandler(LOG_FILE)
handler.setFormatter(formatter)
logger.addHandler(handler)

client_ip=sys.argv[1]
direction=sys.argv[2]
pps=sys.argv[3]
action=sys.argv[4]

logger.info(" - " . join(sys.argv))

if action == "unban":
    try:
       print("unban ip {} direction {} pps {} action {}".format(
           client_ip, direction, pps, action))
    except Exception as e:
        logger.info("Unban action failed, possible error: " + str(e))

    sys.exit(0)

elif action == "ban" or action == "attack_details":
    try:
        print("ban ip {} direction {} pps {} action {}".format(
           client_ip, direction, pps, action))
    except Exception as e:
        logger.info("Ban action failed, possible error: " + str(e))

    sys.exit(0)


