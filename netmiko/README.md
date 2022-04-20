## Introduction

I will show you how to use scripting across multiple devices using netmiko
Specifically, how to log into a list of cisco devices and perform a set of show cmds
Output is captured on a file, no explicit loggin of the screen is needed

## General info

This script has 2 loops. 
The outer loop logins to the devices. 
The inner loop executes the cmd list

Tested success on Nexus7000, ASR1004, C9500, c4500, C9300, c3850
1st for loop logs into device; 2nd for loop runs the cmd list for the current device
Cmd list do not need to include "term len 0" (longer output is parsed automatically by Netmiko)
Create dictionary "connect_info" and use as input for method ConnectHandler()
Some cmd list are privilleged, thats why we need to specify secret password and do enable

## Important!!
```
This Jupyter notebook contains 2 scripts:
a) netmiko_shCmd_multidev
b) netmiko_shCmd_multidev (with password encryption using fernet)
```

## Setup
```
install using "pip install netmiko"
Fill in username, password, secret, path for file capture/logging
Run in conda/ or any python IDE
```

