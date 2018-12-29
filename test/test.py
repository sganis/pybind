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
    print("Person 10: " + str(e["10"]))
    print(f"Person 9: { e['9'] }")

    for p in people:
        print(p.hello())
    assert len(e.people()) == 10
    assert repr(e) == 'example.Example class'

if __name__ == '__main__':
    import sys
    import os
    import pytest
    DIR = os.path.dirname(os.path.realpath(__file__))
    sys.path.append(DIR)
    sys.path.append(os.path.abspath("."))
    pytest.main(['-s', __file__])
