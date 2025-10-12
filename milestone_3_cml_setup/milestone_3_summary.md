🧠 Milestone 3: Cisco Modeling Labs (CML) Install and Refplat Import

📅 Date: Sat Oct 12, 2025
🧩 Session Goal: Complete installation, image import, and verification of Cisco Modeling Labs (CML) on the bare-metal Ubuntu Server host.

1️⃣ Environment Context

Host: Intel NUC running Ubuntu Server 24.04

CML Version: 2.9.0+build.3

Virtualization Backend: KVM (libvirt)

VM Name: cml-server

Image Mount Path: /var/lib/cml/images/refplat-20250616-fcs.iso

2️⃣ Key Steps Completed

Verified VM definition

Dumped XML via virsh dumpxml cml-server

Cleaned up invalid ide controller and replaced with valid sata config.

Redeployed fixed domain definition with:

sudo virsh define ~/cml-server-fixed.xml


Attached Refplat ISO

Transferred image via SCP from Windows host:

scp "$env:USERPROFILE\Desktop\refplat-20250616-fcs.iso" cmladmin@10.229.1.90:/var/lib/cml/images/


Validated successful mount:

sudo virsh dumpxml cml-server | grep refplat


Ran Refplat Copy

ISO recognized as /dev/sr0

Copy executed automatically by the CML system process:

*** Copying file objects from ISO image...
Volume id 'REFPLAT'
Copying complete
Restarting controller to reload images...
Exiting with code 0


Rebooted and Verified

sudo virsh reboot cml-server

CML GUI verified at https://10.229.1.88

System Status: All components (KVM, CPUs, Images, Docker, Fabric, etc.) green.

Image Definitions and Node Definitions loaded ✅

3️⃣ Verification Checks

Verified via GUI:

Node Definitions: IOSv, IOSvL2, CSR1000v, XRv9000, CAT8000v, ASAv, Alpine, FRR, Chrome.

Images and definitions show under Tools → System → Node and Image Definitions.

CLI validation:

sudo virsh list --all
sudo virsh dumpxml cml-server | grep refplat


All services and images operational.

4️⃣ Backup

Created clean image snapshot:

sudo virsh shutdown cml-server
sudo cp /var/lib/libvirt/images/cml-server.qcow2 /var/lib/libvirt/images/cml-server_clean-install.qcow2
sudo virsh start cml-server

5️⃣ Outcome

✅ CML fully operational
✅ Refplat imported
✅ Node and image definitions verified
✅ Backup created as restore point

🟢 Status: Complete
🕐 Next Session: Build and verify first topology (IOSv + Alpine + External Connector ping test)