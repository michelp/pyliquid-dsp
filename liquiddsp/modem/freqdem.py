from liquiddsp import _cffi
from liquiddsp._cffi import cdef, ffi

cdef('typedef struct freqdem_s * freqdem;')

cdef("""typedef enum {
    LIQUID_FREQDEM_PLL=0,       // phase-locked loop
    LIQUID_FREQDEM_DELAYCONJ    // delay/conjugate method
} liquid_freqdem_type;
""")
PLL = 0   # not sure how to avoid this defining these constants
DELAYCONJ = 1


@cdef('freqdem freqdem_create(float _kf, liquid_freqdem_type _type);')
def create(kf, typ):
    return ffi.gc(_cffi.lib.freqdem_create(kf, typ), freqdem_destroy)


@cdef('void freqdem_destroy(freqdem _q);')
def destroy(q):
    return _cffi.lib.freqdem_destroy(q)


@cdef('void freqdem_print(freqdem _q);')
def print(q):
    return _cffi.lib.freqdem_print(q)


@cdef('void freqdem_reset(freqdem _q);')
def reset(q):
    return _cffi.lib.freqdem_reset(q)


@cdef('void freqdem_demodulate(freqdem _q, liquid_float_complex _r, float * _m);')
def demodulate(q, r, m):
    return _cffi.lib.freqdem_reset(q, r, m)

