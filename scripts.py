#instance mgmt usgin boto3 
import boto3
# Create an EC2 client
ec2 = boto3.client('ec2')
# Function to start instances
def start_instances(instance_ids):
    ec2.start_instances(InstanceIds=instance_ids)
    print("Instances started:", instance_ids)
# Function to stop instances
def stop_instances(instance_ids):
    ec2.stop_instances(InstanceIds=instance_ids)
    print("Instances stopped:", instance_ids)
# Provide your instance IDs
instance_ids = ['i-0abcd1234efgh5678']
# Start or Stop instances
start_instances(instance_ids)
stop_instances(instance_ids)



# create dirctory and move files
import os
import shutil
# Create a new directory
os.makedirs("backup", exist_ok=True)
# Move a file to the new directory
shutil.move("example.txt", "backup/example.txt")
print("File moved to backup directory.")


#createin backup script
import os
import shutil
from datetime import datetime
# Get the current date and time
current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
# Define source and destination
source_dir = "data"
backup_dir = f"backup_{current_time}"
# Copy the entire directory
shutil.copytree(source_dir, backup_dir)
print(f"Backup created at: {backup_dir}")


#log monitoring for error 
import time
# Open the log file
with open("application.log", "r") as file:
    # Go to the end of the file
    file.seek(0, os.SEEK_END)
    while True:
        line = file.readline()
        if "ERROR" in line:
            print(f"Error found: {line.strip()}")
        time.sleep(1)



#atutoamting docker commnads
import subprocess
# Run a Docker container
command = "docker run -d nginx"
process = subprocess.run(command, shell=True)
if process.returncode == 0:
    print("Docker container started successfully.")
else:
    print("Failed to start Docker container.")


