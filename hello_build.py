#!/usr/bin/env python

from cffi import FFI
ffibuilder = FFI()

ffibuilder.set_source("_hello",
    r"""
    char const* greet()
    {
        return "Greetings!";
    }
""",
    libraries=[])

ffibuilder.cdef("""
    char const *greet(void);
""")

if __name__ == "__main__":
    ffibuilder.compile(verbose=True)
