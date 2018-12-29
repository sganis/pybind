#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# python3 -m pytest ./test.py -s

def test_example():
    import example
    e = example.Example()
    p = e.person()
    print(p.hello())
    assert p.hello() == 'I am a person id 0'
    people = e.people()
    assert len(people) == 10
    print(type(people))

    for p in people:
        print(p.hello())
#    assert len(e.people()) == 10


if __name__ == '__main__':
    import example
    print(dir(example))
    import sys
    print(sys.path)
    import os
    import pytest
    DIR = os.path.dirname(os.path.realpath(__file__))
    sys.path.append(DIR)
    pytest.main(['-s', __file__])
