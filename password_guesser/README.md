## Introduction

I will show you how to use a script to go through a list of password. 
Your organization have a alot of different Cisco console passwords used and over time, the list
could get very long. If you lose tacacs access, your only way is to access via console
copy and pasting passwords to and from is messy.
This script tries passwords from a list until a successful login


## General info

Please customised these 2 vairables in the script: 'pass_list' and 'user'
Upon successful login, It sends password to the screen
Usually used when trying console passwords in cisco, usually after 3 tries, 
the console returns a blank screen, script overcomes this by sending a 
carriage return to return to the password prompt


**Sequence:**

1. Amend 'pass_list' and 'user'
2. Connect to Cisco device via console
3. Run the script
4. Script runs through 'pass_list' until login is successful
5. Scripts shows you the password it used for logging in
6. Script stops


## Setup
```
Run script from SecureCrt app. Goto 'Script' -> 'Run..' -> pwd_guesser.py
or
Run from SecureCrt button bar
```

