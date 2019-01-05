import sys, os
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))

import _example
from _example import *

__all__ = ['Example', 'main','__version__']

class Employee(Person):
    def __init__(self, id):
        id = "I am an employee"
        Person.__init__(self, id)


def main():
    e = Example()
    print('example is working!')
    print(e.hello())

__version__ = _example.__version__

if __name__ == '__main__':
    main()
