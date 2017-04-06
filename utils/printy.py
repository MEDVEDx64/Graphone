# A simple logger

from time import time

_mask = 0xff
_timebase = time()


def _print(msg, bit):
    if not bit & _mask:
        return

    print(('%.3f' % (time() - _timebase)) + ' ' + msg)


def crit(msg):
    _print('!!! ' + msg, 1)


def err(msg):
    _print('! ' + msg, 2)


def warn(msg):
    _print('? ' + msg, 4)


def info(msg):
    _print('> ' + msg, 8)


def debug(msg):
    _print('@ ' + msg, 16)
