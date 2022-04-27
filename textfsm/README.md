## Introduction

I will show you how to take unstructured data(cli output) and convert it to structured data(ie csv) using textfsm
TextFSM is a library created by Google to handle output from network devices

## General info

Script autmotically selects the template to use based on the keywords found inside the input file
It supports the conversion of 5 common cisco clis into csvs

```
show cdp neighbor detail
show version
show ip interface brief
show ip bgp summary
show inventory
```

Script requires the following 2 files to run:
The Input file:
This is the raw cli output from one or more devices 
The Template file:
The template file is the parser, like an interpreter for the particular command “show version”)
One template file to one “show command”, 
So “show version output” requires an equivalent “show version template”

## Setup
```
install using "pip install textfsm"
Make sure to put the script and its templates in the same directory
Run and provide the input file to script
Run in conda/ or any python IDE
Result is output into a csv file
```

