from liquiddsp import _cffi
from liquiddsp._cffi import cdef, ffi


cdef('typedef struct freqmod_s * freqmod;')

@cdef('freqmod freqmod_create(float _kf);')
def create(kf):
    return ffi.gc(_cffi.lib.freqmod_create(kf), freqmod_destroy)


@cdef('void freqmod_destroy(freqmod _q);')
def destroy(q):
    return _cffi.lib.freqmod_destroy(q)


@cdef('void freqmod_print(freqmod _q);')
def print(q):
    return _cffi.lib.freqmod_print(q)


@cdef('void freqmod_reset(freqmod _q);')
def reset(q):
    return _cffi.lib.freqmod_reset(q)


@cdef('void freqmod_modulate(freqmod _q, float _m, liquid_float_complex * _s);')
def modulate(q, m, s):
    return _cffi.lib.freqmod_modulate(q, m, s)


def modulate_buffer(mod, buff, num_samples):
    return ffi.gc(_cffi.lib.modulate_buffer(mod, buff, num_samples), _cffi.lib.free)


