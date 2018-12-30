#include <pybind11/pybind11.h>
//#include <pybind11/stl.h>
//#include <pybind11/operators.h>
#include "example.h"
#include "person.h"

namespace py = pybind11;

void init_example(py::module &m) {
    py::class_<Example>(m, "Example")
        .def(py::init())
        .def("hello", &Example::hello)
        .def("person", &Example::person)
        .def("people", &Example::people)
        .def("__str__", &Example::str)
        .def("__repr__", &Example::repr)
        .def("__getitem__", &Example::operator[]);
}
