#!/usr/bin/env python3
# build script
#
import sys
import os
import time
import shutil

DIR   = os.path.dirname(os.path.realpath(__file__))
SRC   = os.path.realpath(f'{DIR}/..')
BUILD = os.path.realpath(f'{DIR}/../build')
WHEEL = os.path.realpath(f'{DIR}/../pack/dist')
TEST  = os.path.realpath(f'{DIR}/../test/test.py')

def build():
    t = time.time()
    print('Building release mode...')

    if os.path.isdir(BUILD):
        shutil.rmtree(BUILD)
    os.mkdir(BUILD)
    os.chdir(f'{BUILD}')

    if os.name == 'nt':
        # os.system(f'cmake {SRC} -G "Visual Studio 14" -A x64')
        # os.system(f'cmake --build . --target ALL_BUILD --config Release --parallel 8 -- -verbosity:minimal')
        os.system(f'cmake {SRC} -G Ninja -DCMAKE_BUILD_TYPE=Release && ninja')
    else:
        os.system(f'cmake {SRC} -G Ninja -DCMAKE_BUILD_TYPE=Release && ninja')

    elapsed = time.strftime('%M:%S', time.gmtime(time.time()-t))

    print(f'Binaries    : {BUILD}')
    print(f'Python wheel: {WHEEL}')
    print(f'Time elapsed: {elapsed} (mm:ss)')
    print('Done.')

def test():
    os.system(f'{ sys.executable } {TEST}')

if __name__ == '__main__':	
        build()
        test()

		
	
