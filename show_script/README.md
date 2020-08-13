## Introduction

Performing any network changes, network engineer often need to perform pre and post network checks on the network device. A list of 'show commands' is usually prepared before the network change. The network engineer compares the output from this list to verify if the change is executed properly 



## General info
This script is based on SecureCrt python API, it is based on 'send' and 'expect' principle. 

For example, in Telnet, a script could start with 'telnet 1.1.1.1', the script 'expects' a 'password' to be returned to by server(1.1.1.1), when server prompts for password, script sends telnet password.

Every device has a different prompt. Linux server has '$', cisco is '#', juniper is '>'. This script starts by 'capturing and storing the prompt in a variable', so that script will understand when the output stops and when to send the next line of show commands

**Sequence:**

1. Prepare the show_command list
2. Start 'log session'
3. Run the script
4. Script prompts you for the show_command list
5. Select the show_command list and script executes
6. Script stops when end of file is reached
7. Stop 'log session'



## Setup
```
Run script from SecureCrt app. Goto 'Script' -> 'Run..' -> sh_cmd-all_devices2.py
or
Run from SecureCrt button bar
```



## Sample screen shots

![image-20200813125036454](C:\Users\ES\AppData\Roaming\Typora\typora-user-images\image-20200813125036454.png)



![image-20200813125212968](C:\Users\ES\AppData\Roaming\Typora\typora-user-images\image-20200813125212968.png)