#!/usr/bin/env python3
# build script
#
import sys
import os
import platform
import time

BUILD_DIR = 'build'
DIR = os.path.dirname(os.path.realpath(__file__))

def build():	
	t = time.time()
	print('Building...')
	
	p = platform.system()
	
	assert not os.path.exists(BUILD_DIR)

	if p == 'Linux' or p == 'Mac':
		os.system('rm -rf {0} && mkdir -p {0}'.format(BUILD_DIR))
		os.chdir(BUILD_DIR)
		os.system('cmake ../.. && make -j8')
		
	elif p == 'Windows':
		os.system('if exist "{0}" rd /s /q "{0}"'.format(BUILD_DIR))
		os.system('md "{}"'.format(BUILD_DIR))
		os.chdir(BUILD_DIR)
		os.system('cmake ../.. && make -j8')
		
	else:
		print('os not supported')
		assert False

	print('\nDone.')
	print('Binaries    : {}'.format(os.path.realpath('.')))
	print('Python wheel: {}'.format(os.path.realpath('../../pack/dist')))
	print('Time elapsed: [hh:mm:ss]: {}'.format(
		time.strftime('%M:%S', time.gmtime(time.time()-t)) ))


if __name__ == '__main__':	
	build()

		
	