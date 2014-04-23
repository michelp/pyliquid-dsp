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
def mod_print(q):
    return _cffi.lib.freqmod_print(q)


@cdef('void freqmod_reset(freqmod _q);')
def reset(q):
    return _cffi.lib.freqmod_reset(q)


@cdef('void freqmod_modulate(freqmod _q, float _m, liquid_float_complex * _s);')
def modulate(q, m, s):
    return _cffi.lib.freqmod_modulate(q, m, s)


@cdef('void freqmod_modulate_block(freqmod _q, float * _m, unsigned int _n, liquid_float_complex * _s);')
def modulate_block(mod, message, signal):
    message_addr = ffi.cast('float *', message.__array_interface__['data'][0])
    signal_addr = ffi.cast('liquid_float_complex *', signal.__array_interface__['data'][0])
    return _cffi.lib.freqmod_modulate_block(mod, message_addr, len(message), signal_addr)


