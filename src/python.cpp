/*************************************
 * Python API
 * **********************************/
#include "example.h"
#include "person.h"
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/operators.h>

namespace py = pybind11;

PYBIND11_MODULE(_example, m) {

    py::class_<Example>(m, "Example")
            .def(py::init())
            .def("hello", &Example::hello)
            .def("person", &Example::person)
            .def("people", &Example::people)
            .def("__str__", &Example::str)
            .def("__repr__", &Example::repr)
            .def("__getitem__", &Example::operator[]);

    py::class_<Person>(m, "Person")
            .def(py::init())
            .def(py::init<const std::string&>())
            .def("__str__", &Person::hello)
            .def("__repr__", &Person::hello)
            .def("hello", &Person::hello);

}
