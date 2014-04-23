"""\
Frequency Demodulator

Usage:
  fm.py [options]
  fm.py (-h | --help)
  fm.py --version

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
    return docopt(__doc__, version='FM 0.1')


def run(args):
    outfile = sys.stdout if args['--file'] == '-' else open(args['--file'], 'wb')
    modem = liquiddsp.modem.FM()
    while True:
        data = array('I')
        data.read(sys.stdin, 1024)
        if not data:
            return
        outfile.write(modem.dem(data))


def main():
    args = get_args()
    run(args)


if __name__ == '__main__':
    main()
