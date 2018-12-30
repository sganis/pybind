#!/bin/sh
# cleanup script

DIR="$( cd "$( dirname "$0" )" && pwd )"
rm -rfv $DIR/../build
find $DIR/.. | grep "/build-" | xargs /bin/rm -rfv
find $DIR/.. | grep "/build/" | xargs /bin/rm -rfv
find $DIR/.. | grep "__pycache__" | xargs /bin/rm -rfv
find $DIR/.. | grep "\.pytest_" | xargs /bin/rm -rfv
find $DIR/.. | grep "\.egg-info" | xargs /bin/rm -rfv
find $DIR/.. \( \
	-name "*.uncrustify" \
	-o -name "*.dump" \
	-o -name "*.o" \
        \) | xargs /bin/rm -rfv

