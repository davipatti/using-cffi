#!/usr/bin/env python

from cffi import FFI
ffibuilder = FFI()

cpp = r"""
#include <iostream>
int greet()
{
    std::cout << "Hello, World!";
    return 0;
}
"""

ffibuilder.set_source("_hello", cpp, libraries=['iostream.h'])

ffibuilder.cdef("""
    int const *greet(void);
""")

if __name__ == "__main__":
    ffibuilder.compile(verbose=True)
