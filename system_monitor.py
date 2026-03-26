import os
import platform
import socket
from datetime import datetime
print("----SYSTEM INFO----")
now = datetime.now()
print("Date & Time:",now.strftime("%Y-%m-%d  %H:%M:%S"))

hostname=socket.gethostname()
print("Hostname:",hostname)
print("python version:",platform.python_version())
user =os.getenv("USER") or os.getenv("USERNAME")
print("current user:",user)
files=os.listdir(".")
print("\nFiles in directory")
for file in files:
 print("-",file)
print("\nTotal Files:",len(files))

name=input("Enter your name:")
print("Hello ! Welcome to the system monitoring tool")

