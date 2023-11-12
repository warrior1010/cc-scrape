import ipaddress
import random

def generate_ip_address(quantity, address_type):
    ip_list = []

    for _ in range(quantity):
        if address_type == 'ipv4':
            ip = ".".join(str(random.randint(0, 255)) for _ in range(4))
            ip_list.append(ip)
        elif address_type == 'ipv6':
            blocks = [format(random.randint(0, 65535), 'x') for _ in range(8)]
            ip = ":".join(blocks)
            ip_list.append(ip)

    return ip_list

def generate_ip_range(start_ip, end_ip, address_type):
    start = ipaddress.ip_address(start_ip)
    end = ipaddress.ip_address(end_ip)
    ip_list = []

    for ip in range(int(start), int(end) + 1):
        if address_type == 'ipv4':
            ip_list.append(str(ipaddress.IPv4Address(ip)))
        elif address_type == 'ipv6':
            ip_list.append(str(ipaddress.IPv6Address(ip)))

    return ip_list

print("SK LIVES IP TOOL")
print("Choose an option:")
print("1. Generate individual IP addresses")
print("2. Generate a range of IP addresses")
choice = input("Enter your choice (1 or 2): ")

if choice == '1':
    quantity = int(input("Enter the quantity of IP addresses to generate: "))
    print("Choose the address type:")
    print("1. IPv4")
    print("2. IPv6")
    address_choice = input("Enter your choice (1 or 2): ")
    if address_choice == '1':
        address_type = 'ipv4'
    elif address_choice == '2':
        address_type = 'ipv6'
    else:
        print("Invalid choice. Please select either 1 or 2.")
        exit()

    ip_addresses = generate_ip_address(quantity, address_type)
    with open("ip.txt", "w") as file:
        for ip in ip_addresses:
            file.write(ip + "\n")

    print(f"{quantity} {address_type} addresses generated and saved in 'ip.txt' file.")

elif choice == '2':
    start_ip = input("Enter the starting IP address: ")
    end_ip = input("Enter the ending IP address: ")
    print("Choose the address type:")
    print("1. IPv4")
    print("2. IPv6")
    address_choice = input("Enter your choice (1 or 2): ")
    if address_choice == '1':
        address_type = 'ipv4'
    elif address_choice == '2':
        address_type = 'ipv6'
    else:
        print("Invalid choice. Please select either 1 or 2.")
        exit()

    ip_range = generate_ip_range(start_ip, end_ip, address_type)
    with open("ip.txt", "w") as file:
        for ip in ip_range:
            file.write(ip + "\n")

    print(f"{len(ip_range)} {address_type} addresses generated and saved in 'ip.txt' file.")

else:
    print("Invalid choice. Please select either 1 or 2.")
