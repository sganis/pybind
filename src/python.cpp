/*************************************
 * Python API
 * **********************************/
#include <pybind11/pybind11.h>

#ifdef _MSC_VER
#define sscanf sscanf_s
#endif

namespace py = pybind11;
void init_example(py::module &);
void init_person(py::module &);

PYBIND11_MODULE(example, m) {
    init_example(m);
    init_person(m);
}


