#!/bin/sh
for i in `cat student-list.txt`; do
	python excel_job.py $i
done
