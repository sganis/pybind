#!/bin/sh
#
# Run uncrustify, a c++ code beautifier.
# Use uncrustify.cfg config file
# Author: San	
# Date:   17 Sep 2017
#

if [ $# -lt 1 ];then
	echo "usage: $0 <project-path>"
	exit 1
fi

DIR="$( cd "$( dirname "$0" )" && pwd )"

echo "running uncrustify $1 ..."
file_list=`find $1 -type f \( -name "*.h" -o -name "*.cpp" \) | grep -v "\.lex\.\|\.yac\."`
for f in $file_list; do  
	$DIR/uncrustify -c $DIR/uncrustify.cfg --no-backup --if-changed "$f" 
done 

echo "exit code from uncrustify: $?"

# overwrite exit code so we can run this script after build 
# and warnings don't stop build
exit 0

