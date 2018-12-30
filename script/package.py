#!/usr/bin/env python3
# Make python package
#
import sys
import os

assert len(sys.argv) > 1
BUILD=sys.argv[1]
DIR = os.path.dirname(os.path.realpath(__file__))

def package():	
	print('Packaging...')	
	
	if os.name == 'nt':
		os.system(fr'copy {BUILD}\example.dll {DIR}\..\pack\example\_example.pyd')
	else: # posix or mac
		os.system(f'cp -v {BUILD}/libexample.so {DIR}/../pack/example/_example.so')

	os.chdir(f'{DIR}/../pack')
	os.system(f'{ sys.executable } setup.py sdist bdist_wheel')
	print('Done.')

if __name__ == '__main__':	
	package()

		