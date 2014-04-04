"""\
Frequency Demodulator

Usage:
  freqdem.py [options]
  freqdem.py (-h | --help)
  freqdem.py --version

Options:
  -h --help                Show this screen.
  -v --version             Show version.
  -f --file=<f>            File to write samples to [default: -].
"""
import sys
import liquiddsp
from array import array
from docopt import docopt


def get_args():
    return docopt(__doc__, version='Freqdem 0.1')


def run(args):
    outfile = sys.stdout if args['--file'] == '-' else open(args['--file'], 'wb')
    freqdem = liquiddsp.modem.freqdem_create(0.1, 1)
    while True:
        data = array('I')
        data.read(sys.stdin, 1024)
        if not data:
            return
        addr, length = data.buffer_info()
        outfile.write(liquiddsp.freqdem_demodulate_buffer(freqdem, addr, length))

def main():
    args = get_args()
    run(args)


if __name__ == '__main__':
    main()
