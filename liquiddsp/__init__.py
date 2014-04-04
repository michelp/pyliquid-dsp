from ._cffi import ffi, ptop

import liquiddsp._cffi

import modem

# compilation happens here in verify(),
# all C code must be defined at this point
# and only after here may the library functions
# and constants be accessed. hence the many import
# name tricks used through the implementation

# http://explosm.net/comics/420/

liquiddsp._cffi.lib = lib = ffi.verify("""
#include <complex.h>
#include <liquid/liquid.h>

""", libraries=['liquid'])
