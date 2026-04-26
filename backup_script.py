import os
import shutil
from datetime import datetime

# Define the source directory that will be backed up
source_folder = "source_folder"

# Define the destination directory where backups will be stored
backup_folder = "backup_folder"

print("Starting backup process...")

# Check if the source directory exists
if not os.path.exists(source_folder):
    print("Error: Source folder does not exist.")
    exit()

# Create the backup directory if it does not exist
if not os.path.exists(backup_folder):
    os.makedirs(backup_folder)

# Generate a timestamp for the backup folder name
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# Create a unique backup folder name using the timestamp
backup_name = "backup_" + timestamp

# Combine backup directory and folder name into a full path
backup_path = os.path.join(backup_folder, backup_name)

try:
    # Copy the entire source directory to the backup location
    shutil.copytree(source_folder, backup_path)

    print("Backup completed successfully.")
    print("Backup location:", backup_path)

# Handle errors that may occur during the backup process
except Exception as error:
    print("Backup failed.")
    print("Error:", error)