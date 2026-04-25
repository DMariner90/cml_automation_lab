YANG Endpoint Discovery Method

1. Start with the parent RESTCONF path.
   Example:
   /restconf/data/Cisco-IOS-XE-native:native/interface

2. Send GET first.
   Never PATCH blind.

3. Read the top-level JSON key.
   Example:
   Cisco-IOS-XE-native:interface

4. Identify container/list/key.
   Example:
   interface -> GigabitEthernet -> name

5. GET the specific list entry.
   Example:
   /restconf/data/Cisco-IOS-XE-native:native/interface/GigabitEthernet=2

6. Copy the returned JSON shape.

7. Remove everything except the fields you want to change.

8. PATCH the exact list-entry URL.

9. Verify with GET.

10. Save the working URL, payload, and error notes.
