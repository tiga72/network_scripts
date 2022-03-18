## Introduction

The cisco’s “sh cdp nei detail” cmd outputs all connected devices info line by line
It can be very hard to view
This shell script to convert this output into csv for easy viewing



## General info

This script looks into the current directory and captures all the file names. 
Except for the script name itself. 
It then process each file and generates a csv equivalent of it 


**Sequence:**

1. Create a directory specifically for running this script: 'script_folder'
2. Inside 'script_folder', place the shell inside
3. Copy cdp log from my local computer to the 'script_folder' directory
4. Use csplit cmd to split them into individual files
5. Remove first file 'xx00'
6. At Linux Run the script
7. Script stops
8. Join all csv file together with linux cat cmd

* For commands needed, please refer to the actual script itself


## Setup
```
Run script from Linux terminal, 'bash multi_cdp.sh'
```

