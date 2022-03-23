<<<<<<< HEAD
# $language = "python"
# $interface = "1.0"

# logs into multiple devices via dev_list.txt(1 at a time) and then 
# runs a set of cmds on each via cmds_for_each_device.txt
# Use jump server at windows WSL

# Need to specify a directory to host 2 files for this script
# The 2 files need to be named: dev_list.txt and cmds_for_each_device.txt

code = "password123"

def check_prompt():
    global g_index
    crt.Screen.Send("\n")
    crt.Screen.WaitForCursor() # readstring captures all string in rawResult after cursor position change is detected
    rawResult = crt.Screen.ReadString(["#", ">"])# Stops reading when it sees # or >
    g_index = crt.Screen.MatchIndex	# MatchIndex is a property of ReadString. Returns integer. Here, "#" is 1; ">" is 2	
    return g_index;

def main():
    for dev in open("C:\\Users\\limengse\\scripts\\rw\\dev_list.txt", "r"): 
        # 1st loop focuses on device list; 2nd loop, runs whole cmd set on each device
        crt.Screen.Send("ssh limengse@" + dev + "\n")
        nIndex = crt.Screen.WaitForStrings(["yes/no", "assword","onnection refused"], 20,False)
        if (nIndex == 0): # Set of actions if connection timeout
            crt.Screen.Send("\x03")
            return
        elif nIndex == 1: # Set of actions if "yes/no"
            crt.Screen.Send("yes" + "\r")
            crt.Screen.WaitForString("assword", 5, False)
            crt.Screen.Send(code + "\r")
        elif nIndex == 2:
            crt.Screen.Send(code + "\r")
        elif nIndex == 3: # Go to next device if "onnection refused"
            continue

        chk_prompt = check_prompt()
        if chk_prompt == 2:
            crt.Screen.Send("en" + "\r")
            crt.Screen.WaitForString("assword", 5, False)
            crt.Screen.Send(code + "\r")
        crt.Sleep(500)

        for cmd in open("C:\\Users\\limengse\\scripts\\rw\\cmds_for_each_device.txt", "r"):
            crt.Screen.Send("\n")
            nIndex1 = crt.Screen.WaitForStrings(["#", ">"])
            if (nIndex1 == 0):
                crt.Screen.Send("\x03")
                return
            elif nIndex1 == 1: # Set of actions if "#"
                crt.Screen.Send(cmd + "\r")

        crt.Screen.Send("exit" + "\r") # After running thr all cmds, send exit to get out
        crt.Screen.WaitForString("$") # Wait for device closing messages(2) to be all sent
        crt.Sleep(200) # waits brief moment before going to next device

    crt.Screen.Send('echo -en "\007"' + '\r') # sends a rings once everything finishes
main()

=======
# $language = "python"
# $interface = "1.0"

# logs into multiple devices via dev_list.txt(1 at a time) and then 
# runs a set of cmds on each via cmds_for_each_device.txt
# Use jump server at windows WSL

# Need to specify a directory to host 2 files for this script
# The 2 files need to be named: dev_list.txt and cmds_for_each_device.txt

code = "password123"

def check_prompt():
    global g_index
    crt.Screen.Send("\n")
    crt.Screen.WaitForCursor() # readstring captures all string in rawResult after cursor position change is detected
    rawResult = crt.Screen.ReadString(["#", ">"])# Stops reading when it sees # or >
    g_index = crt.Screen.MatchIndex	# MatchIndex is a property of ReadString. Returns integer. Here, "#" is 1; ">" is 2	
    return g_index;

def main():
    for dev in open("C:\\Users\\limengse\\scripts\\rw\\dev_list.txt", "r"): 
        # 1st loop focuses on device list; 2nd loop, runs whole cmd set on each device
        crt.Screen.Send("ssh limengse@" + dev + "\n")
        nIndex = crt.Screen.WaitForStrings(["yes/no", "assword","onnection refused"], 20,False)
        if (nIndex == 0): # Set of actions if connection timeout
            crt.Screen.Send("\x03")
            return
        elif nIndex == 1: # Set of actions if "yes/no"
            crt.Screen.Send("yes" + "\r")
            crt.Screen.WaitForString("assword", 5, False)
            crt.Screen.Send(code + "\r")
        elif nIndex == 2:
            crt.Screen.Send(code + "\r")
        elif nIndex == 3: # Go to next device if "onnection refused"
            continue

        chk_prompt = check_prompt()
        if chk_prompt == 2:
            crt.Screen.Send("en" + "\r")
            crt.Screen.WaitForString("assword", 5, False)
            crt.Screen.Send(code + "\r")
        crt.Sleep(500)

        for cmd in open("C:\\Users\\limengse\\scripts\\rw\\cmds_for_each_device.txt", "r"):
            crt.Screen.Send("\n")
            nIndex1 = crt.Screen.WaitForStrings(["#", ">"])
            if (nIndex1 == 0):
                crt.Screen.Send("\x03")
                return
            elif nIndex1 == 1: # Set of actions if "#"
                crt.Screen.Send(cmd + "\r")

        crt.Screen.Send("exit" + "\r") # After running thr all cmds, send exit to get out
        crt.Screen.WaitForString("$") # Wait for device closing messages(2) to be all sent
        crt.Sleep(200) # waits brief moment before going to next device

    crt.Screen.Send('echo -en "\007"' + '\r') # sends a rings once everything finishes
main()

>>>>>>> 3cf4207476f109ce53822b126a591f9d7c899707
