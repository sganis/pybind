#include <pybind11/pybind11.h>
//#include <pybind11/stl.h>
//#include <pybind11/operators.h>
#include "person.h"

namespace py = pybind11;

void init_person(py::module &m) {
    py::class_<Person>(m, "Person")
            .def(py::init())
            .def(py::init<const std::string&>())
            .def("__str__", &Person::hello)
            .def("__repr__", &Person::hello)
            .def("hello", &Person::hello);
}
