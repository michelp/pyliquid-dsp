from ._cffi import ffi, ptop

import liquiddsp._cffi

ffi.cdef('typedef ... liquid_float_complex;')

import modem

# compilation happens here in verify(),
# all C code must be defined at this point
# and only after here may the library functions
# and constants be accessed. hence the many import
# name tricks used through the implementation

# http://explosm.net/comics/420/

ffi.cdef("""
void free(void *ptr);
""")

liquiddsp._cffi.lib = lib = ffi.verify("""
#include <liquid/liquid.h>
#include <stdlib.h>

""", libraries=['liquid'])
