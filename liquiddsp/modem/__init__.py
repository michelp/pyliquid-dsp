import numpy
import liquiddsp
from liquiddsp import ffi
from liquiddsp.modem import freqmod, freqdem
from liquiddsp.util import lazy_property

class Modem(object):
    """ Abstract modem class. """

    def mod(self, buff, **kw):
        """ Modulate a signal in buff.  Return a new buffer of the modulated signal. """
        raise NotImplemented


    def dem(self, buff, **kw):
        """ Demodulate a signal in buff. """
        raise NotImplemented


class FM(Modem):
    """ Frequency Modulation. """

    def __init__(self, mod_index=0.1, dem_index=None):
        self.mod_index = mod_index
        self.dem_index = mod_index if dem_index is None else dem_index

    @lazy_property
    def modulator(self):
        return freqmodcreate(self.mod_index)

    @lazy_property
    def demodulator(self):
        return freqdem.create(self.dem_index)

    def mod(self, message, signal=None):
        """ Modulate a message and return a signal, 
        optionally overwrite the signal provided.. """
        assert message.dtype == numpy.float32
        if signal is None:
            signal = numpy.empty(len(message), dtype=numpy.complex64)
        else:
            assert len(signal) >= len(message) and signal.dtype = numpy.complex64
        freqmod.modulate_block(self.modulator, message, len(signal), signal)
        return signal


    def dem(self, signal, message=None):
        """ Demodulate a signal and return a message,
        optionally overwrite the message provided.
        """
        assert signal.dtype == numpy.complex64
        if message is None:
            message = numpy.empty(len(signal), dtype=numpy.float32)
        else:
            assert len(message) >= len(signal) and message.dtype = numpy.float32
        freqdem.demodulate_block(self.demodulator, signal, len(signal), message)
        return message


class AM(Modem):
    """ Amplitude Modulation. """
    suppressed_carrier = False
#    type=pyliquiddsp.AMPMODEM_DSB

    def __init__(self, mod_index, carrier_frequency):
        self.mod_index = mod_index
        self.kf = kf

    def mod(self, buff, **kw):
        """ Modulate a signal in buff. """
        raise NotImplemented


    def dem(self, buff, **kw):
        """ Demodulate a signal in buff. """
        raise NotImplemented


class USB(AM):
    """ Upper Side Band Modulation. """
    suppressed_carrier = True
#    type=pyliquiddsp.AMPMODEM_LSB


class LSB(AM):
    """ Lower Side Band Modulation. """
    suppressed_carrier = True
#    type=pyliquiddsp.AMPMODEM_USB


class PSK(Modem):
    pass


class DPSK(Modem):
    pass


class ASK(Modem):
    pass


class QAM(Modem):
    pass


class APSK(Modem):
    pass


class BPSK(Modem):
    pass


class QPSK(Modem):
    pass


class OOK(Modem):
    pass


class SQAM32(Modem):
    pass


class SQAM128(Modem):
    pass


class V29(Modem):
    pass


class ARB16OPT(Modem):
    pass


class ARB32OPT(Modem):
    pass


class ARB64OPT(Modem):
    pass


class ARB128OPT(Modem):
    pass


class ARB256OPT(Modem):
    pass


class ARB64VT(Modem):
    pass
 
