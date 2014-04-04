from liquiddsp import _cffi
from liquiddsp._cffi import cdef, ffi


cdef('typedef struct freqmod_s * freqmod;')
cdef('typedef ... liquid_float_complex;')

cdef("""typedef enum {
    LIQUID_FREQDEM_PLL=0,       // phase-locked loop
    LIQUID_FREQDEM_DELAYCONJ    // delay/conjugate method
} liquid_freqdem_type;
""")
LIQUID_FREQDEM_PLL = 0   # not sure how to avoid this defining these constants
LIQUID_FREQDEM_DELAYCONJ = 1


@cdef('freqmod freqmod_create(float _kf);')
def freqmod_create(kf):
    return ffi.gc(_cffi.lib.freqmod_create(kf), freqmod_destroy)


@cdef('void freqmod_destroy(freqmod _q);')
def freqmod_destroy(q):
    return _cffi.lib.freqmod_destroy(q)


@cdef('void freqmod_print(freqmod _q);')
def freqmod_print(q):
    return _cffi.lib.freqmod_print(q)


@cdef('void freqmod_reset(freqmod _q);')
def freqmod_reset(q):
    return _cffi.lib.freqmod_reset(q)


@cdef('void freqmod_modulate(freqmod _q, float _m, liquid_float_complex * _s);')
def freqmod_modulate(q, m, s):
    return _cffi.lib.freqmod_modulate(q, m, s)


def freqmod_modulate_buffer(mod, buff, num_samples):
    return ffi.gc(_cffi.lib.modulate_buffer(mod, buff, num_samples), _cffi.lib.free)


cdef('typedef struct freqdem_s * freqdem;')


@cdef('freqdem freqdem_create(float _kf, liquid_freqdem_type _type);')
def freqdem_create(kf, typ):
    return ffi.gc(_cffi.lib.freqdem_create(kf, typ), freqdem_destroy)


@cdef('void freqdem_destroy(freqdem _q);')
def freqdem_destroy(q):
    return _cffi.lib.freqdem_destroy(q)


@cdef('void freqdem_print(freqdem _q);')
def freqdem_print(q):
    return _cffi.lib.freqdem_print(q)


@cdef('void freqdem_reset(freqdem _q);')
def freqdem_reset(q):
    return _cffi.lib.freqdem_reset(q)


@cdef('void freqdem_demodulate(freqdem _q, liquid_float_complex _r, float * _m);')
def freqdem_demodulate(q, r, m):
    return _cffi.lib.freqdem_reset(q, r, m)

