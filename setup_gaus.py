from distutils.core import setup
from Cython.Build import cythonize

import Cython.Compiler.Options
Cython.Compiler.Options.annotate = True

import numpy
setup(ext_modules=cythonize("gauss_seidel_cython.pyx", compiler_directives={"language_level": "3"}, annotate=True), 
                            include_dirs=[numpy.get_include()])
