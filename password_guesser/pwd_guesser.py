# $language = "python"
# $interface = "1.0"

# Script tries a passwords from a list until a successful login
# Upon successful login, It sends password to the screen
# Need to customised the password list and the user in script

pass_list = ['papa',
'mama',
'daddy',
'haha',
'hehe',
'hoho',
'mimi',
'cisco',
'juniper'
]

count = 0
user = "Manager"

for passwd in pass_list:
	pwd = pass_list[count]
	count = count + 1
	while True:
		index1 = crt.Screen.WaitForStrings(["Username:","login:"],2,False)
		if (index1 == 0):
			crt.Screen.Send('\r')
		if (index1 == 1):
			break
		if (index1 == 2):
			break
	index1 = crt.Screen.WaitForStrings(["Username:","login:"],2,False)
	if (index1 == 0):
		crt.Screen.Send(user + '\r')	
	if (index1 == 1):
		crt.Screen.Send(user + '\r')
	if (index1 == 2):
		crt.Screen.Send(user + '\r')
	crt.Screen.WaitForString("assword:")
	crt.Sleep(200)
	crt.Screen.Send(pwd + '\r')
	nIndex = crt.Screen.WaitForStrings(["incorrec", "invalid", "#", ">"])
	if (nIndex == 1):
		continue
	elif (nIndex == 2):
		continue
	elif (nIndex == 3):
		break
	elif (nIndex == 4):
		break
	crt.Sleep(200)	
crt.Sleep(700)
crt.Screen.Send("# password is " + pwd + '\r')
