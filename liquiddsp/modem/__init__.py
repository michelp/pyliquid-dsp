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
    type=pyliquiddsp.FREQDEM_PLL

    def __init__(self, carrier_frequency, mod_index=0.1,
                 dem_index=None, dem_type=liquiddsp.modem.freqdem.PLL):
        self.mod_index = mod_index
        self.dem_index = dem_index
        self.dem_type = dem_type

    @lazy_property
    def modulator(self):
        return liquiddsp.modem.freqmod.create(self.mod_index)

    @lazy_property
    def demodulator(self):
        return liquiddsp.modem.freqdem.create(self.dem_index, self.dem_type)

    def mod(self, buff, **kw):
        """ Modulate a signal in buff. """
        raise NotImplemented

    def dem(self, buff):
        """ Demodulate buff, returning a new buffer with the demodulated signal. """
        addr, length = buff.buffer_info()
        return liquiddsp.freqdem_demodulate_buffer(freqdem, addr, length)


class AM(Modem):
    """ Amplitude Modulation. """
    suppressed_carrier = False
    type=pyliquiddsp.AMPMODEM_DSB

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
    type=pyliquiddsp.AMPMODEM_LSB


class LSB(AM):
    """ Lower Side Band Modulation. """
    suppressed_carrier = True
    type=pyliquiddsp.AMPMODEM_USB


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
 
