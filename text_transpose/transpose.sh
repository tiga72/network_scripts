#!/bin/bash

#<<Global>>
# Script contains 2 awk function:
# 	v2h: transpose a vertical range of text as a horizontal range
# 	h2v: transpose a horizontal range of text as a vertical range
#
# An if statement checks the type of input file and calls the appropriate awk function
# grep -q returns 1 if comma is found; grep -c (count) would work also; 
# if comma is found, then input file is "horizontal"; h2v function will be called
# Else input file will be "vertical"; v2h function will be called
# input_file is read into bash as $1
# How to run script: bash transpose.sh input_file
# =============================================
# <<vertical to horizon (v2h)>>
# Typical usage: Convert from cisco config into csv for readability 
# Important!! Input syntax requirements: Sections(vertical) of file to be separated by newline ("")
#---------------------
# Input example(vertical): 
# interface Gi0/0
# ip address 1.1.1.1
# description ex1
# 
# interface Gi0/1
# ip address 2.2.2.2
# description ex2
#---------------------
# bash syntax:
# awk -v FS="\n" -v RS="" '{print $1","$2","$3","$4","$5","$6","$7","$8","$9","$10}' input_file | tr -s ',' ','
#
# $1 to $10: Accepts/caters up to 10 fields/columns 
# Example: 3 fields results in 7 extra commas printed to the eol; ie 4 fields -> 6 extra commas; and so on
# Any no.of repeated commas is reomved by squeeze(tr -s option). Removes repeated instances of commas.
# =============================================
# =============================================
# <<horizon to vert (h2v)>>
# Typical usage: Convert from csv to cisco config (for config preparation/runbook)
# Important!! Input syntax requirements: Each line and field/column separated by comma(Includes eol)
#---------------------
# Input example(horizontal): 
# interface Gi0/0,ip address 1.1.1.1, description ex1,
# interface Gi0/1,ip address 2.2.2.2, description ex2,
#---------------------
# bash syntax: 
# awk -v RS="," -v FS="," '{print}' input_file
# =============================================

echo "Processing..."
if grep -c "," $1; then
    awk -v RS="," '{print}' $1 > $"$1_h2v"
	echo "Output file is "$1_h2v""
else
    awk -v FS="\n" -v RS="" '{print $1","$2","$3","$4","$5","$6","$7","$8","$9","$10}' $1 | tr -s ',' ',' > $"$1_v2h".csv
	echo "Output file is "$1_v2h".csv"
fi
echo -en "\007"


