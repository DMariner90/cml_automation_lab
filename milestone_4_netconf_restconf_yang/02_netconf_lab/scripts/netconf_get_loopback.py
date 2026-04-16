from ncclient import manager

ROUTER = {
    "host": "10.229.1.91",
    "port": 830,
    "username": "david",
    "password": "cisco123",
    "hostkey_verify": False
}

filter_xml = """
<interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
  <interface>
    <name>Loopback10</name>
  </interface>
</interfaces>
"""

print("NETCONF get-config (running) for Loopback10")
with manager.connect(**ROUTER) as m:
    reply = m.get_config(source="running", filter=("subtree", filter_xml))
    print(reply.xml)
