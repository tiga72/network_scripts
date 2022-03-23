## Introduction

I will show you how to use a script to do an 'intelligent search'

Sometimes, we need to do multiline grep of on files
Grep barely can do this properly without churning out alot of false positives
egrep "string1|string2" inputfile
Greping this way is also an OR condition (Generating false positives)

## General info

Cisco uses hierarchy cfg structure demostrating parent/child relationships

interface Gi0/1
 description Test
 ip address 1.1.1.1 255.255.255.0

Example: 'interface' is the 'parent string' and 'description' 
and 'ip address' are 'child strings'

Use cases:
Maybe we want to check which are the interfaces that were shutdown
or just which have 'switchport access vlan 89'


**Sequence:**

Script accepts either a 2 keywords or 3 keywords search 
(to be separated by comma and space sensitive)

1. Goto directory that contains the files you want to do the search on
2. Under same directory. Run the script
4. First prompt appears, you may enter 1 or more filenames(separated by space)
5. Second prompt, enter 2 keywords or 3 keywords search(separated by comma)
6. Script runs and output results and results matches(count)


## Setup
```
Run script from SecureCrt app. Goto 'Script' -> 'Run..' -> awk_search4.py
or
Run from SecureCrt button bar
```

