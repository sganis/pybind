#!/usr/bin/env python3
# build script
#
import sys
import os
import time

BUILD_DIR = 'build'
DIR = os.path.dirname(os.path.realpath(__file__))

def build():	
	t = time.time()
	print('Building release mode...')

	assert not os.path.exists(BUILD_DIR)

	if os.name == 'nt':
		os.system(f'if exist "{BUILD_DIR}" rd /s /q "{BUILD_DIR}"')
		os.system(fr'md "{BUILD_DIR}\Release"')
		os.chdir(f'{BUILD_DIR}')
		os.system('cmake ../.. -G "Visual Studio 14" -A x64')
		# os.system('msbuild /P:Configuration=Release ALL_BUILD.vcxproj')
		os.system('cmake --build . --target ALL_BUILD --config Release --parallel 8')
	else:
		os.system(f'rm -rf {BUILD_DIR} && mkdir -p {BUILD_DIR}')
		os.chdir(BUILD_DIR)
		os.system('cmake ../.. && make -j8')

	print('\nDone.')
	print('Binaries    : {}'.format(os.path.realpath('.')))
	print('Python wheel: {}'.format(os.path.realpath('../../pack/dist')))
	print('Time elapsed: {} (mm:ss)'.format(
		time.strftime('%M:%S', time.gmtime(time.time()-t)) ))


if __name__ == '__main__':	
	build()

		
	