#!/bin/sh
if [ "$(uname)" == "Darwin" ]; then
        CMD=python3
else
        CMD=python
fi
for i in `cat student-list.txt`; do
	$CMD excel_job.py $i
done
