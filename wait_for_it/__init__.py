import time

from wait_for_it._version import __version__, __version_info__


def to_be_true(func):
    while True:
        if func():
            return True
        time.sleep(0.01)
