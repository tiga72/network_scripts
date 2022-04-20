## Introduction

This script will transpose vertically arranged text horizontally or vice versa automatically
It reads the input file and based on the input file type, it will perform the neceessary conversion
Use cases:
To convert interface related configs from csv into a config file or
To put interface config into excel for documentation or planning


## General info

This script consists of 2 awk commands.
One will perform text/file arrangement horizontally as a csv
The other will perform text/file arrangement vertically (like a cisco interface config)

The 2 awk commands:
	v2h: transpose a vertical range of text as a horizontal range
	h2v: transpose a horizontal range of text as a vertical range

An if statement checks the type of input file and calls the appropriate awk function
grep -q returns 1 if comma is found; grep -c (count) would work also; 
if comma is found, then input file is "horizontal"; h2v function will be called
Else input file will be "vertical"; v2h function will be called
input_file is read into bash as $1

How to run script: bash transpose.sh input_file

**Sequence/setup:**

1. input file requirements

vertical input file:
Important!! Input syntax requirements: Sections(vertical) of file to be separated by newline ("")


Input example(vertical): 
interface Gi0/0
ip address 1.1.1.1
description ex1

interface Gi0/1
ip address 2.2.2.2
description ex2


horizontal input file:
Important!! Input syntax requirements: Each line and field/column separated by comma(Includes eol)

Input example(horizontal): 
interface Gi0/0,ip address 1.1.1.1, description ex1,
interface Gi0/1,ip address 2.2.2.2, description ex2,


## Setup
```
Run script from Linux terminal, 'bash transpose.sh [input_file]'
```

