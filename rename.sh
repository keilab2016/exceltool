#!/bin/sh
for i in 1*.pdf; do
	id=`echo $i | sed -e 's,.pdf,,g'`
	echo "cp -p $i ../b${id}_0_assignsubmission_file_b$id.pdf"
done
