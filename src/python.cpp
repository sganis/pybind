/***********************************************************************
 * Copyright 2019, San. All rights reserved.
 * Author:  San
 * Date:    01/04/2019
 * Python API
 ************************************/
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "version.h"
#include "example.h"

#ifdef _MSC_VER
# define sscanf sscanf_s
#endif  // ifdef _MSC_VER

namespace py = pybind11;

PYBIND11_MODULE(_example, m) {
    m.doc() =
        R"pbdoc(
        Example module documentation
        ----------------------------
        .. currentmodule:: example
        .. autosummary::
           :toctree: _generate
    )pbdoc";
    m.attr("__version__") = VERSION;

    py::class_<Example>(m, "Example")
    .def(py::init())
    .def("hello",       &Example::hello)

    // pointer always by reference
    .def("people",      &Example::people, py::return_value_policy::reference)
    .def("__str__",     &Example::str)
    .def("__repr__",    &Example::repr)
    .def("__getitem__", &Example::operator[]);

    py::class_<Person>(m, "Person")

    // constructors
    .def(py::init())
    .def(py::init<const std::string&>())

    // properties
    .def_property("id", &Person::id, &Person::set_id)

    // dunder methods
    .def("__repr__",    &Person::to_json)
    .def("__str__",     &Person::hello)

    // methods
    .def("hello",       &Person::hello)
    .def("to_json",     &Person::to_json)
    .def("type",        &Person::type)

    // lambda function
    .def("only_pybind", [](const Person& p) {
        return "Person " + p.id() + ": only pybind method";
    });

    py::class_<Programmer, Person>(m, "Programmer")

    // constructors
    .def(py::init<const std::string&>());
}
