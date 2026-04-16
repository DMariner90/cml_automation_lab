NETCONF / RESTCONF Quick Configuration & Verification Guide
💩 1. Enable on IOS XE
configure terminal
!
hostname <HOSTNAME>
ip domain-name lab.local
!
crypto key generate rsa modulus 2048
ip ssh version 2
!
username admin privilege 15 secret <PASSWORD>
!
netconf-yang
ip http secure-server
ip http authentication local
restconf
!
line vty 0 4
 login local
 transport input ssh
end
write memory
🧩 2. Basic Verification (Device-Side)
Check	Command	Expected Result
SSH enabled	show ip ssh	“SSH Enabled – version 2.0”
NETCONF active	show platform software yang-management process	netconf process running
RESTCONF active	show ip http server secure status	Secure server enabled (443)
Confirm TCP ports	`show sockets summary	i 22	830	443`	All three ports listening
🔌 3. Basic Verification (Dev-Side)
Test	Command	Expected
Ping device	ping <IP>	Replies received
SSH	ssh admin@<IP>	Login prompt
NETCONF port check	nc -zv <IP> 830	“succeeded”
RESTCONF via curl	curl -k -u admin:<pw> https://<IP>/restconf/data/ietf-interfaces:interfaces	XML or JSON interface list
🛠️ 4. Sample Python Connectivity Tests

NETCONF – capabilities

from ncclient import manager
with manager.connect(host="<IP>", port=830, username="admin", password="<pw>", hostkey_verify=False) as m:
    for cap in m.server_capabilities:
        print(cap)

RESTCONF – quick GET

curl -k -u admin:<pw> https://<IP>/restconf/data/ietf-interfaces:interfaces
✅ Working = You See

<ok/> on NETCONF edits

JSON or XML data from RESTCONF GET

Router shows expected config via show run | sec interface

Use this page as a fast reference to enable, verify, and test NETCONF / RESTCONF from scratch