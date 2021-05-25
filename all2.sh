#!/bin/sh
STUDENTLIST=student-list.txt
if [ $# -gt 0 -a -f $1 ]; then
	STUDENTLIST=$1
fi
j=0
list=()
for i in `cat $STUDENTLIST`; do
	list=(${list[@]} $i)
	let j++
	if [ $j == 15 ]; then
		python excel_job.py ${list[@]}
		j=0
		list=()
	fi
done
if [ $j != 0 ]; then
	python excel_job.py ${list[@]}
fi
