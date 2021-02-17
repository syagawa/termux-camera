import subprocess
from time import sleep
from subprocess import check_call
from datetime import datetime
import os

def shot():
    print("shot!")
    t = datetime.now().isoformat()
    if os.path.exists("./images") == False:
        os.makedirs("./images")
    filename = "./images/%s.jpg" % t
    subprocess.call(["pkill", "com.termux.api"])
    subprocess.call(["termux-camera-photo", "-c", "0", filename])


def shots(count, interval):
    for i in range(count):
        shot()
        sleep(interval)

def setShots(count, interval):
    n = count
    i = interval
    def f():
        shots(n, i)
    return f

shots(10, 2)

