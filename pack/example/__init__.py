import sys, os
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))

from _example import Example, Person

__all__ = ['Example', 'main']

class Employee(Person):
    def __init__(self, id):
        id = "I am an employee"
        Person.__init__(self, id)


def main():
    e = Example()
    print('example is working!')
    print(e.hello())


if __name__ == '__main__':
    main()
