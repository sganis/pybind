#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# python3 -m pytest ./test.py -s

import sys
import os
import json
import pytest

DIR = os.path.dirname(os.path.realpath(__file__))
sys.path.append(DIR)
sys.path.append(os.path.abspath(DIR + "/../pack/build/lib"))

def test_example():
    print()
    import example
    e = example.Example()
    assert repr(e) == 'example.Example class'
#    print(dir(example))


    people = e.people()
    assert len(people) == 10
    p1 = e['1']
    print(p1)
    print(p1.__class__)
    print(p1.__class__.__name__)
    print(p1.to_json())
    j = json.loads(p1.to_json())
    print(type(j))

    prog = e["1000"];

    print(f"Person 1 str    : { str(e['1']) }")
    print(f"Person 8 print  : { e['8'] }")
    print(f"Person 9 repr   : { repr(e['9']) }")
    print(f"Programmer repr : { repr(prog) }")
    print(f"Programmer str  : { str(prog) }")
    print(f"Programmer hello(): { prog.hello() }")
    print(f"Person 1 type     :", e['1'].type())
    print(f"Programmer type   :", prog.type())

    p1.id = '999'
    print(f"Person 1 id    : { p1.id }")
    print(p1.only_pybind())

    for k in sorted(people, key=lambda x: int(x)):
        print(k, people[k])

#    j = json.loads(repr(people).replace('\'','"'))
#    print(json.dumps(j, indent=4))



if __name__ == '__main__':
    pytest.main(['-s', __file__])
