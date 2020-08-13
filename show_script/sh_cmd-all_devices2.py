# $language = "python"
# $interface = "1.0"

# captures the full prompt(var full_prompt) string including the escape character
# exmple: das1.nj3#, Full prompt is das1.nj3#
# exmple: das1.nj4. The full prompt(2 lines, but it doesnt matter) is:
# {master:0}
# autojuco@das1.nj4>
# This sh cmds can be used with any terminal that ends with either ["#",">","$"]

import re

def main():
    objTab = crt.GetScriptTab()
    objTab.Screen.Synchronous = True
    prompt = ["#",">","$"]
    selected_prompt = ""


    def get_prompt():
        global full_prompt								# global variable is re-used later at line 44( inside for loop)
        objTab.Screen.Send('\r')						# function starts by carriage return and the next line captures the prompt
        nIndex = objTab.Screen.WaitForStrings(prompt,1)	# nIndex returns 1,2,3
        if (nIndex == 1):
            selected_prompt = "#"
        elif nIndex == 2:
            selected_prompt = ">"
        else:
            selected_prompt = "$"    

        objTab.Screen.Send('\r')
        tmpResult = crt.Screen.ReadString(prompt,1)

        full_prompt = tmpResult + selected_prompt
        return;
    
    shCmdList = crt.Dialog.FileOpenDialog(title="slect file",filter="Text Files(*.txt)|*.txt||")	# ask user for show command list
    cmd = open(shCmdList, "r")

    get_prompt()	# runs the pre-defined function
	
    for line in cmd:
		crt.Screen.Send(line + '\r')
		crt.Screen.WaitForString(full_prompt)	# Device churns out information based on the 'show command' and waits for prompt 
		crt.Sleep(1200)		    # For every show command sent and its assoicated output, it waits 1.2 secs before going to next show command
        
    objTab.Screen.Synchronous = False

    
main()
