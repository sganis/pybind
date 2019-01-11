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

    py::class_<Example> ex(m, "Example");
    ex.def(py::init());
    ex.def("hello",       &Example::hello);
    ex.def("people",      &Example::people,
           py::return_value_policy::reference);
    ex.def("__str__",     &Example::str);
    ex.def("__repr__",    &Example::repr);
    ex.def("__getitem__", &Example::operator[]);

    py::class_<Person> pe(m, "Person");
    pe.def(py::init());
    pe.def(py::init<const std::string&>(), py::arg("id"),
           "Constructor");
    pe.def_property("id", &Person::id, &Person::set_id);
    pe.def("__repr__",    &Person::to_json);
    pe.def("__str__",     &Person::hello);
    pe.def("hello",       &Person::hello);
    pe.def("to_json",     &Person::to_json);
    pe.def("type",        &Person::type);
    pe.def("only_pybind", [](const Person& p) {
        return "Person " + p.id() + ": only pybind method";
    });

    py::class_<Programmer, Person> pr(m, "Programmer");
    pr.def(py::init<const std::string&>(), py::arg("id"));
}
