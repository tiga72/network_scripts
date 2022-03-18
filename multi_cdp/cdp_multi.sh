#!/bin/bash
# This scripts processes oputput from cisco devices with cmd sh cdp neighbors detail
# Values obtained have heading and/or trailing spaces and needs to be removed
# Tested on 6500,4451,C9500,Nexus, c3850
# This script is the variation of the orginal; Able to process multiple files(inside the same working dir)
# To run: bash cdp.sh
# output file format is: cdp2_<inputfilename>.csv
# -------------------------------------
# 1. Use script to capture multiple devices using cmd 'sh cdp nei detail' -> combined.log
# 2. Copy combined.log into same directory as this script
# 3. Split combined.log into smaller multiple files; Use: csplit -z shCdpNeiDetail.log /"term len 0"/ '{*}'
# file separator is "term len 0"
# 4. Delete/move combined.log elsewhere 
# 5. Make sure all smaller multiple files + this script file inside a folder
# 6. Run script; After which you will have multiple csv files. 
# 7. Use cmd to combined all csvs as one: cat *csv > combined.csv
# -------------------------------------

# "grep -v cdp" : Means to exclude script's own name while copying ls into var files
# var files will contain all file names of the smaller files, used for script looping thru these files

files=$(ls /mnt/c/Users/limengse/scripts/shell_script/working | grep -v cdp_multi);

for val in $files; do
	echo "Processing..."

	# get local_host column
	LOCAL_HOST=$(egrep '#sh cdp' $val | awk -v FS="#" '{print $1}');

	# get remote_host column
	REMOTE_HOST_SPACE=$(grep 'Device' $val | awk -v FS=":" '{print $NF}');
	REMOTE_HOST="$(echo -e "${REMOTE_HOST_SPACE}" | sed -e 's/^[[:space:]]*//' -e 's/[[:space:]]*$//')";

	# get platform column
	TYPE_SPACE=$(grep 'Platform' $val | awk -F"," '{print $1}' | awk -F: '{print $NF}');
	TYPE="$(echo -e "${TYPE_SPACE}" | sed -e 's/^[[:space:]]*//' -e 's/[[:space:]]*$//')";

	# get local_intf column
	LOCAL_INTF_SPACE=$(grep 'outgoing port' $val | awk -F"," '{print $1}' | awk '{print $NF}');
	LOCAL_INTF="$(echo -e "${LOCAL_INTF_SPACE}" | sed -e 's/^[[:space:]]*//' -e 's/[[:space:]]*$//')";

	# get remote_intf column
	REMOTE_INTF_SPACE=$(grep 'outgoing port' $val | awk -F"," '{print $NF}' | awk -F: '{print $NF}');
	REMOTE_INTF="$(echo -e "${REMOTE_INTF_SPACE}" | sed -e 's/^[[:space:]]*//' -e 's/[[:space:]]*$//')";

	# get remote_ip column
	IP_SPACE=$(awk 'f{print;f=0} /t address/{f=1}' $val | awk '{print $NF}');
	IP="$(echo -e "${IP_SPACE}" | sed -e 's/^[[:space:]]*//' -e 's/[[:space:]]*$//')";

	# Join all values(column by column horizontally) and output as cdp1(temp)
	paste -d , <(echo "$REMOTE_HOST") <(echo "$TYPE") <(echo "$LOCAL_INTF") <(echo "$REMOTE_INTF") <(echo "$IP") > cdp1;

	# Join everything together: add header to cdp1 and output as csv
	awk -F"," -v localHost=$LOCAL_HOST 'BEGIN {print "local_host"",""remote_host"",""type"",""local_intf"",""remote_intf"",""ip"} {print localHost "," $0}' cdp1 > $"cdp2_$val".csv;

	# aim was to get dynamic/different output names based on the input file; Appends cdp2 to inputfilename
	# Remove the Byte-order mark "ï»¿" from file
	sed -i 's/\xEF\xBB\xBF//g' "cdp2_$val".csv;

	#rm cdp1;
	echo "Formatted cdp nei in csv is "cdp2_$val".csv"
done
