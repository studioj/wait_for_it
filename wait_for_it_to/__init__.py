import time

from wait_for_it_to._version import __version__, __version_info__


def be_true(func):
    start = time.time()
    while True:
        result = func()
        if result:
            return True
        if time.time() > start + 10:
            msg = "expected something that evaluates to True, but got %s instead" % str(result)
            raise TimeoutError(msg)
        time.sleep(0.01)
