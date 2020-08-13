# This script pings a list of ips(from ping-host.txt) every 5 secs
# Each time the script runs, timestamp is logged
# Use 'ctrl-C' to manually stop script
# ping-host.txt format: ip-host, host-name
# Useful in monitoring of critical devices when performing complex network change

import subprocess
import os
import time
import sys


def main():
        check = "0 received, 100% packet loss"

        while True:
                print "\n================================="
                now = time.strftime("%c")
                print (now + "\n")
                file = open("/home/elim2/py-script/ping-host.txt", "r")
                for line in file:
                        y = line.split(",")
                        ip1 = y[0]
                        host1 = y[1]
                        str1 = str(host1 + "is alive")
                        str2 = str(host1 + "is unreachable")
                        ping_process = subprocess.Popen(['ping', '-q', '-c', '1', '-w', '1', ip1], stdout=subprocess.PIPE)
                        stdout = ping_process.stdout.read()
                        if not(check in stdout):
                                str1 = str1.replace("\n", " ")
                                print(str1)
                        else:
                                str2 = str2.replace("\n", " ")
                                print(str2)
                time.sleep(5)
main()
