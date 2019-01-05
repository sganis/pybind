#!/bin/sh
#
# Run static code analyzer
# uncrustify + cpplint.py
# Author: san
# Date: Jan 4 2019

if [ $# -lt 1 ];then
    echo "usage: $0 <project-path>"
    exit 1
fi

DIR="$( cd "$( dirname "$0" )" && pwd )"

$DIR/uncrustify.sh $1
#$DIR/cppcheck.sh $1
$DIR/cpplint.sh $1


