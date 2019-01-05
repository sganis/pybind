#!/usr/bin/env python3
# build script
#
import sys
import os
import time

DIR = os.path.dirname(os.path.realpath(__file__))
	
def build(BUILD_DIR):	
	t = time.time()
	print('Building release mode...')
	
	SRC = os.path.realpath(f'{DIR}/..')

	if os.name == 'nt':
		os.system(fr'md "{BUILD_DIR}\Release"')
		os.chdir(f'{BUILD_DIR}')
		os.system(f'cmake {SRC} -G "Visual Studio 14" -A x64')
		os.system('cmake --build . --target ALL_BUILD --config Release --parallel 8 -- -verbosity:minimal')
	else:
		os.chdir(BUILD_DIR)
		os.system(f'cmake {SRC} && make -j8')

	print('\nDone.')
	print('Binaries    : {}'.format(os.path.realpath('.')))
	print('Python wheel: {}'.format(os.path.realpath('../../pack/dist')))
	print('Time elapsed: {} (mm:ss)'.format(
		time.strftime('%M:%S', time.gmtime(time.time()-t)) ))


if __name__ == '__main__':	

	assert len(sys.argv) > 1 # usage: ./build.py <build_dir>
	BUILD_DIR = os.path.realpath(sys.argv[1])
	build(BUILD_DIR)

		
	