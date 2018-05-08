#!/usr/bin/env python

from _hello import ffi, lib

print ffi.string(lib.greet())
