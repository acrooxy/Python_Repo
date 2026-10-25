import socket
import time
import csv
from datetime import datetime

print("Service Availability Monitor")

host = input("Enter domain or IP: ")

try:
    port = int(input("Enter port, for example 443: "))

    if port < 1 or port > 65535:
        print("Port must be between 1 and 65535.")

    else:
        print("Monitoring started. Press Ctrl+C to stop.")

        while True:
            date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            connection = socket.socket(
                socket.AF_INET,
                socket.SOCK_STREAM
            )
            connection.settimeout(5)

            try:
                connection.connect((host, port))
                status = "AVAILABLE"

            except OSError:
                status = "UNREACHABLE"

            finally:
                connection.close()

            print(date, "-", host, "-", port, "-", status)

            with open("service_results.csv", "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([date, host, port, status])

            time.sleep(10)

except ValueError:
    print("Port must be a number.")

except KeyboardInterrupt:
    print("\nMonitoring stopped.")
