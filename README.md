# AnsibleFest 2018 - Ansible for Network Distributed Denial of Service Mitigation
Files related to AnsibleFest 2018 Session https://agenda.fest.ansible.com/SessionDetail.aspx?id=498179

This repository contains the files for the demonstration of the AnsibleFest 2018 session titled **Ansible for Network Distributed Denial of Service Mitigation**. Please let us know your thoughts in the comments below!!

If you are the impatient kind, skip to the bottom of the page for the combined video for the demonstration. However, since there is no narratives involved in the video, I personally feel it is better to watch the videos one-by-one in the order listed below. 

You can find the VIRL topology file as well as the device configuration in this repository. 

The lab topology involved with video 1 to 6 are listed here: 

![alt text](https://github.com/a10networks/ansiblefest2018/blob/master/Topology_Scenario_1.png "Topology 1")

The lab topology involved with video 7 for on-premise mitigation is here: 

![alt text](https://github.com/a10networks/ansiblefest2018/blob/master/Topology_Scenario_2.png "Topology 1")

### 1. Lab Topology

In the video, the web server uses the Python simple http module to host a web server. The client will generate traffic that traverse thru Transit-3 to Provider-Upstream and Customer-Edge to arrive at the web server. There is a flowspec-server (IOS-XR) that is BGP peered with the Provider-Upstream router as well as the Customer-Edge router. 

The management station and FastNetMon host are both located on the management network not shown in the VIRL design panel. 

[![1. Lab Topology](https://img.youtube.com/vi/3dcADc2G4lA/0.jpg)](https://www.youtube.com/watch?v=3dcADc2G4lA&index=9&t=0s&list=PLAaTeRWIM_wsuW1jO0BE9gbZvvgqDZTIK)

### 2. FastNetMon Banned Action

In this video, you will see the FastNetMon process along with the FastNetMon froent-end client started. Note that FastNetMon can be started as a daemon, but in this case it is started in standard out for demonstration. The FastNetMon configuration under /etc/fastnetmon.conf is modified so that a low PPS count will trigger the banned action. 

I find the client script sometimes do not show the ban or unban, the log under /var/log/fastnetmon.log is a better indication of action. 

[![2. FastNetMon Banned](https://img.youtube.com/vi/gc-q1qqJOtw/0.jpg)](https://www.youtube.com/watch?v=gc-q1qqJOtw&index=8&t=0s&list=PLAaTeRWIM_wsuW1jO0BE9gbZvvgqDZTIK)

### 3. Ansible Playbook Integration

When the banned action is triggered, a script is triggered. By default, this is a shell script. We can place our Playbook inside of this shell script. 

[![3. First Playbook Example](https://img.youtube.com/vi/o-4LIdZchDA/0.jpg)](https://www.youtube.com/watch?v=o-4LIdZchDA&index=7&t=0s&list=PLAaTeRWIM_wsuW1jO0BE9gbZvvgqDZTIK)

### 4. Banned and Unbanned actions

Once the device is banned, you can configure the duration of banned time. Once the timer is up, FastNetMon will continue to check if the violation traffic is still active and determine if it will trigger unban or continue to ban. 

This is where the Ansible idempotent characteristic is really handy. 

[![4. Ban and Unban Actions](https://img.youtube.com/vi/nHwlOupS-gc/0.jpg)](https://www.youtube.com/watch?v=nHwlOupS-gc&index=6&t=0s&list=PLAaTeRWIM_wsuW1jO0BE9gbZvvgqDZTIK)

### 5. Banned and Unbanned Python Script

You can also use a Python script as the banned / unbanned trigger. Ansible's Python API can be a really powerful tool in this scenario. 

[![5. Ban and Unban Python Script](https://img.youtube.com/vi/upiS8cbs2T0/0.jpg)](https://www.youtube.com/watch?v=upiS8cbs2T0&index=5&t=0s&list=PLAaTeRWIM_wsuW1jO0BE9gbZvvgqDZTIK)

### 6. Making Flowspec Changes

FastNetMon has built-in ExaBGP support for Flowspec announcement (and RTBH capability), but in this case, we will use the IOS-XR flowspec speaker to trigger the announcement. Note: 

- The banned host is stored as an environmental variable that is read by Ansible Playbook during run time. 
- In the virtual environment, the device cannot program flows into hardware, therefore you will receive and error for the client both in IOS-XR and IOS. However, the control plane works as expected. 
- I found what I suspect is a bug with iosxr-v where if the destination host is the same as existing, the commit action will error out. 

[![6. Making Flowspec Changes](https://img.youtube.com/vi/U2gFGwh718I/0.jpg)](https://www.youtube.com/watch?v=U2gFGwh718I&index=4&t=0s&list=PLAaTeRWIM_wsuW1jO0BE9gbZvvgqDZTIK)

### 7. On-Premise DDoS Scrubbing 

In the second scenario, we will program a DDoS scrubbing device on-premise. The device is sitting off to the side without being involved in the normal traffic flow. When attack happens, the scrubbing device will announce the prefix via BGP to redirect the particular traffic toward itself and pass back the clean traffic. Note: 

- The scrubbing devices is an A10 TPS device with AxAPI v3. 
- I am using a custom module that you can find in this repository. We are using the cli.deploy capability that executes any CLI commands on the device. You can find the module under the library directory. 
- The playbook is bgp_on_ram.yml. 
- We are assuming the mitigation configuration was already configured, we only need to advertise the BGP host route in order to on-ramp the traffic. 

[![7. On-Premise DDoS Scrubbing](https://img.youtube.com/vi/ITQdyr549pw/0.jpg)](https://www.youtube.com/watch?v=ITQdyr549pw&index=3&t=0s&list=PLAaTeRWIM_wsuW1jO0BE9gbZvvgqDZTIK)


### Combined Videos

This is a video that combines the previous 7 videos. 

[![Combined Demonstration](https://img.youtube.com/vi/Y1kvwbRZKI4/0.jpg)](https://www.youtube.com/watch?v=Y1kvwbRZKI4&index=2&t=0s&list=PLAaTeRWIM_wsuW1jO0BE9gbZvvgqDZTIK)


Thanks for watching, let us know what you think in the comments below! 


