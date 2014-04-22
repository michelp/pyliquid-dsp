from ._cffi import ffi, ptop

import liquiddsp._cffi

cdef('typedef ... liquid_float_complex;')

import modem

# compilation happens here in verify(),
# all C code must be defined at this point
# and only after here may the library functions
# and constants be accessed. hence the many import
# name tricks used through the implementation

# http://explosm.net/comics/420/

ffi.cdef("""
float* demodulate_buffer(freqdem dem, void *buffer, int num_samples);

void free(void *ptr);
""")

liquiddsp._cffi.lib = lib = ffi.verify("""
#include <complex.h>
#include <liquid/liquid.h>
#include <stdlib.h>


float complex* modulate_buffer(freqmod mod, void *buffer, int num_samples) {
    int i;
    float* data = (float*)buffer;
    float complex* r = (float complex*)malloc(num_samples * sizeof(float complex));
    for (i = 0; i < num_samples; i++) {
        freqmod_modulate(mod, data[i], &r[i]);
    }
    return r;
}


float* demodulate_buffer(freqdem dem, void *buffer, int num_samples) {
    int i;
    float complex* data = (float complex*)buffer;
    float* r = (float*)malloc(num_samples * sizeof(float));
    for (i = 0; i < num_samples; i++) {
        freqdem_demodulate(dem, data[i], &r[i]);
    }
    return r;
}


""", libraries=['liquid'])


def freqdem_demodulate_buffer(dem, buff, num_samples):
    return ffi.buffer(ffi.gc(lib.demodulate_buffer(dem, ffi.cast('void*', buff), num_samples), lib.free))
