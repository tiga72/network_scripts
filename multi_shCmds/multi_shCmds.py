# $language = "python"
# $interface = "1.0"

# logs into multiple devices via dev_list.txt(1 at a time) and then 
# runs a set of cmds on each via cmds_for_each_device.txt
# Use jump server at windows WSL

# Need to specify a directory to host 2 files for this script
# The 2 files need to be named: dev_list.txt and cmds_for_each_device.txt

	
objTab = crt.GetScriptTab()  #Returns the tab from which the script was started.
tab = objTab.Screen  #Allows us to type "tab.xxx" instead of "objTab.Screen.xxx"

code = "Alawi@78"
def main():
    for dev in open("C:\\Users\\limengse\\scripts\\rw\\dev_list.txt", "r"): 
        # 1st loop focuses on device list; 2nd loop, runs whole cmd set on each device
    #		tab.Send("\n")
        crt.Screen.Send("ssh Manager@" + dev + "\n")
        nIndex = crt.Screen.WaitForStrings(["yes/no", "assword","onnection refused"], 20,False)
        if (nIndex == 0):
            crt.Screen.Send("\x03")
            return
        elif nIndex == 1:
            crt.Screen.Send("yes" + "\r")
            crt.Screen.WaitForString("assword", 5, False)
            crt.Screen.Send(code + "\r")
        elif nIndex == 2:
            crt.Screen.Send(code + "\r")
        elif nIndex == 3:
            continue
        crt.Sleep(500)
        for cmd in open("C:\\Users\\limengse\\scripts\\rw\\cmds_for_each_device.txt", "r"):
            tab.Send("\n")
            nIndex1 = crt.Screen.WaitForStrings(["#", ">"])
            if (nIndex1 == 0):
                crt.Screen.Send("\x03")
                return
            elif nIndex1 == 1:
                crt.Screen.Send(cmd + "\r")
            elif nIndex1 == 2:
                crt.Screen.Send("en" + "\r")
                crt.Screen.WaitForString("assword", 5, False)
                crt.Screen.Send(code + "\r")
                crt.Screen.Send(cmd + "\r")
            crt.Sleep(500)
main()

