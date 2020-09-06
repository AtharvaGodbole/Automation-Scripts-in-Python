import shutil
import psutil
import requests
import socket

def storage_check(disk):
    du = shutil.disk_usage(disk)
    percent = (du.free/du.total)*100
    return percent < 30

def cpu_check(s):
    fh = psutil.cpu_percent(s)
    return fh < 25

def localhost_check():
    l = socket.gethostbyname("localhost")
    if l == "127.0.0.1":
        return True

def internet_check():
    i = requests.get("http://www.goggle.com")
    if i:
        return True

if storage_check("/"):
    print("Insufficient Storage")
elif not cpu_check(1):
    print("Low CPU Performance")
elif not localhost_check():
    print("Localhost not working")
elif not internet_check():
    print("Not connected to Internet")
else:
    print("Everything is Fine")