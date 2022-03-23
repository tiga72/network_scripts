## Introduction

I will show you how to use scripting across multiple devices. 
Specifically,  how to log into a list of cisco devices and perform a set of show cmds

## General info

This script has 2 loops. 
The outer loop logins to the devices. 
The inner loop executes the cmd list

The script needs 2 input files: device list and cmd list
Both the device list and cmds list have to be specified in the script before you run it. 
To set the path for the 2 files, see line 17 and line 34
Also notice the outer loop is at line 17 and inner loop is at line 34
To set the username and password. See line 15 and line 20

**Sequence:**

1. Setup the 2 input files; set username and password (See General info)
2. Run this in Linux terminal
3. Log the session
4. Run the script
5. Script stops
6. Stop session logging


## Setup
```
Run script from SecureCrt app. Goto 'Script' -> 'Run..' -> multi_shCmds.py
or
Run from SecureCrt button bar
```

