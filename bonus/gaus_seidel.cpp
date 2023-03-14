#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>
#include <algorithm>

namespace py = pybind11;

// Inpu is a pyhon array, and we are returning a python array.
py::array_t<double> gauss_seidel(py::array_t<double> f)
{
    /* Request a buffer descriptor from Python */
    auto f_buf = f.request();
    double* f_data = static_cast<double*>(f_buf.ptr);

    auto shape = f_buf.shape;
    int rows = shape[0];
    int cols = shape[1];

    // https://pybind11.readthedocs.io/en/stable/advanced/pycpp/numpy.html
    py::buffer_info buf{nullptr, sizeof(double), py::format_descriptor<double>::format(), 2, shape, {cols*sizeof(double), sizeof(double)}};
    auto newf = py::array_t<double>(buf);
    // Include the copy, to not mess with the original data
    // I am not sure if that is necessary in the way of calling c from python, but better safe than sorry.
    double* newf_data = static_cast<double*>(newf.request().ptr);

    std::copy(f_data, f_data + rows*cols, newf_data);

    for (int i = 1; i < rows - 1; i++) {
        for (int j = 1; j < cols - 1; j++) {
            newf_data[i*cols+j] = 0.25 * (newf_data[i*cols+j+1] + newf_data[i*cols+j-1] +
                                          newf_data[(i+1)*cols+j] + newf_data[(i-1)*cols+j]);
        }
    }

    return newf;
}

PYBIND11_MODULE(gauss_seidel, m)
{
    m.doc() = "Gauss-Seidel method in Pybind11";
    m.def("gauss_seidel", &gauss_seidel, "Gauss-Seidel method");
}