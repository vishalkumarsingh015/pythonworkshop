import os #importing  a library into your code

print (os.system('df -h'))

import shutil

total, used, free = shutil.disk_usage("C:/") # Replace "C:/" with the drive you want to check

print(f"Total: {total / (1024**3):.2f} GB")
print(f"Used: {used / (1024**3):.2f} GB")
print(f"Free: {free / (1024**3):.2f} GB")

print (os.system('sysinfo'))