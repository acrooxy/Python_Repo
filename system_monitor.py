import psutil

print("System & Network Monitor")

choice = ""

while choice != "0":
    print("\n1. Check CPU")
    print("2. Check RAM")
    print("3. Check disk space")
    print("4. Check network data")
    print("0. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        cpu = psutil.cpu_percent(interval=1)
        print("CPU usage:", cpu, "%")

    elif choice == "2":
        ram = psutil.virtual_memory()

        total = ram.total / (1024 ** 3)
        used = ram.used / (1024 ** 3)

        print("Total RAM:", round(total, 2), "GB")
        print("Used RAM:", round(used, 2), "GB")
        print("RAM usage:", ram.percent, "%")

    elif choice == "3":
        disk = psutil.disk_usage("C:\\")

        total = disk.total / (1024 ** 3)
        free = disk.free / (1024 ** 3)

        print("Total disk space:", round(total, 2), "GB")
        print("Free disk space:", round(free, 2), "GB")
        print("Disk usage:", disk.percent, "%")

    elif choice == "4":
        network = psutil.net_io_counters()

        sent = network.bytes_sent / (1024 ** 2)
        received = network.bytes_recv / (1024 ** 2)

        print("Data sent:", round(sent, 2), "MB")
        print("Data received:", round(received, 2), "MB")

    elif choice == "0":
        print("Goodbye!")

    else:
        print("Invalid option. Try again.")
