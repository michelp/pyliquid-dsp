from liquiddsp import _cffi
from liquiddsp._cffi import cdef, ffi


cdef('typedef struct freqdem_s * freqdem;')


@cdef('freqdem freqdem_create(float _kf);')
def create(kf):
    return ffi.gc(_cffi.lib.freqdem_create(kf), destroy)


@cdef('void freqdem_destroy(freqdem _q);')
def destroy(q):
    return _cffi.lib.freqdem_destroy(q)


@cdef('void freqdem_print(freqdem _q);')
def dem_print(q):
    return _cffi.lib.freqdem_print(q)


@cdef('void freqdem_reset(freqdem _q);')
def reset(q):
    return _cffi.lib.freqdem_reset(q)


@cdef('void freqdem_demodulate(freqdem _q, liquid_float_complex _r, float * _m);')
def demodulate(q, r, m):
    return _cffi.lib.freqdem_reset(q, r, m)


@cdef('void freqdem_demodulate_block(freqdem _q, liquid_float_complex * _r, unsigned int _n, float * _m);')
def demodulate_block(mod, signal, message):
    signal_addr = ffi.cast('liquid_float_complex *', signal.__array_interface__['data'][0])
    message_addr = ffi.cast('float *', message.__array_interface__['data'][0])
    return _cffi.lib.freqdem_demodulate_block(mod, signal_addr, len(signal), message_addr)
