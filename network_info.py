import socket
import psutil

print("Network Information Tool")

computer_name = socket.gethostname()
print("Computer name:", computer_name)

interfaces = psutil.net_if_addrs()
interface_status = psutil.net_if_stats()

for name, addresses in interfaces.items():
    print("\nInterface:", name)

    if name in interface_status:
        if interface_status[name].isup:
            print("Status: Active")
        else:
            print("Status: Inactive")

    for address in addresses:
        if address.family == socket.AF_INET:
            print("IPv4 address:", address.address)
            print("Subnet mask:", address.netmask)

        elif address.family == psutil.AF_LINK:
            print("MAC address:", address.address)
