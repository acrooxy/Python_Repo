import shutil

# Display a message to indicate the script has started
print("Checking disk space...")

# Get disk usage statistics
# total = total disk space
# used = used disk space
# free = free disk space
total, used, free = shutil.disk_usage("/")

# Convert bytes to gigabytes
total_gb = total // (2**30)
used_gb = used // (2**30)
free_gb = free // (2**30)

# Display disk space information
print("Disk Space Report")
print("-----------------")

print("Total space:", total_gb, "GB")
print("Used space:", used_gb, "GB")
print("Free space:", free_gb, "GB")

# Check if free space is below threshold
if free_gb < 5:
    print("Warning: Low disk space.")
else:
    print("Disk space is sufficient.")