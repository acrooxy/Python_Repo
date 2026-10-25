import socket

print("Network Connectivity Checker")

host = input("Enter domain or IP: ")
port_text = input("Enter port, for example 443: ")

try:
    port = int(port_text)

    if port < 1 or port > 65535:
        print("Port must be between 1 and 65535.")

    else:
        ip = socket.gethostbyname(host)
        print("IP address:", ip)

        connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connection.settimeout(5)

        try:
            connection.connect((ip, port))
            print("Connection successful!")
            print("Port", port, "is reachable.")

        except OSError:
            print("Connection failed.")
            print("The service may be unavailable or blocked.")

        finally:
            connection.close()

except ValueError:
    print("Port must be a number.")

except socket.gaierror:
    print("Could not find the IP address.")
    print("Check the domain name or your internet connection.")
