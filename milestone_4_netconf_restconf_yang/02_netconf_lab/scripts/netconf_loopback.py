# This is a simple script that creates a loopback interface on the listed router using NETCONF and XML

from ncclient import manager
from lxml import etree

ROUTER = {
    "host" : "10.229.1.91",
    "port" : 830,
    "username" : "david",
    "password" : "cisco123",
    "hostkey_verify" : False
}


# Create a loopback interface with XML/NETCONF as per details below: 
loopback_cfg = """
<config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    <interface>
      <name>Loopback10</name>
      <description>NETCONF Created</description>
      <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">
        ianaift:softwareLoopback
      </type>
      <enabled>true</enabled>
      <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
        <address>
          <ip>10.10.10.10</ip>
          <netmask>255.255.255.255</netmask>
        </address>
      </ipv4>
    </interface>
  </interfaces>
</config>
"""


# Connect to the router with NETCONF
with manager.connect(**ROUTER) as router:
    print("Connect via NETCONF")
    # Push the configuration XML
    reply = router.edit_config(target="running", config=loopback_cfg)
    print(reply.xml)

    
    