#!/bin/sh
DIR="$( cd "$( dirname "$0" )" && pwd )"
BUILD=$1
cp -v $BUILD/libexample.so $DIR/../pack/example/_example.so
cd $DIR/../pack
python3 setup.py sdist bdist_wheel
cd -
