# $language = "python3"
# $interface = "1.0"

# <<Problem>>
# Typical issue. When using egrep "interface|shutdown" router.cfg is not accurate, 
# It also matches many interfaces that are not shutdown
# -----------------------------------------------------
# <<Description>>
# Example: Script will only show interfaces that are shutdown, removing false positives
# Script accepts either a 2 keywords or 3 keywords search (to be separated by comma and space sensitive)
# Script will not perform a '1 keyword' search (easily do it in CLI)
# Lastly, it also prints the no of counts from the search (based on the parent string)
# -----------------------------------------------------
# <<Example>>
# Cisco hierarchy structure where interface has child attributes like description
# Script accept one or more filename
# Filenames must be separated by a space 
# For example for 3 keyword search, I might want to search 'interface', 'description' and 'ip address'
# Order of entry is important: interface,description,ip address
# Here, 'interface' is the 'parent string' and 'description' and 'ip address' are 'child strings'


SCRIPT_TAB = crt.GetScriptTab()

global filename
global searchStr

filename = str(crt.Dialog.Prompt("Enter one or more file separated by space"))
searchStr = str(crt.Dialog.Prompt("Enter parent and child string/strings to search separated by commas"))
searchStr = list(searchStr.split(","))

def awk_search_2():
	awk2 = f"awk 'FNR==1 {{ print \n; print FILENAME }} /{searchStr[0]}/{{ var1=$0; next }} /{searchStr[1]}/{{ print var1; print $0; count++ }} END {{print \n; print \"Matches = \", count}}' {filename}"
	crt.Screen.Send(awk2 + "\n")
	return;
	
def awk_search_3():
	awk3 = f"awk 'FNR==1 {{ print \n; print FILENAME }} /{searchStr[0]}/{{ var1=$0; next }} /{searchStr[1]}/{{var2=$0; next}} /{searchStr[2]}/{{ print var1; print var2; print $0; count++ }} END {{print \n; print \"Matches = \", count}}' {filename}"
	crt.Screen.Send(awk3 + "\n")
	return;
	
def main():

	if len(searchStr) == 2:
		awk_search_2()

	if len(searchStr) == 3:
		awk_search_3()

main()
