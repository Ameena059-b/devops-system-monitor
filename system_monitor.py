import os
import platform
import socket
from datetime import datetime
def system_info():
print("----SYSTEM INFO---")
now = datetime.now()
print("Date & Time:",now.strftime("%Y-%m-%d  %H:%M:%S"))

hostname=socket.gethostname()
print("Hostname",hostname)
print("python version:",platform.python_version())
user =os.getenv("USER") or os.getenv("USERNAME"))
printf("current user:",user)
files=os.listdir(",")
print(""\nFiles in irectory")
for file in files:
print("-",fiile)
print("\nTotal Files:",len(files))

def user_input_feature():
print("/n--USER INPUT--")
name=input("Enter your name:")
print(f"Hello,{name}! Welcome to the system monitoring tool")
if_name_=="_main_":
system_info()
user_input_feature()
