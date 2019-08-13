import time

from wait_for_it_to._version import __version__, __version_info__


def be_true(func, timeout=10):
    """
    waits until func evaluates to True
    raises an exception when the timeout expires

    :param timeout: a timeout in seconds
    :param func: an executable object

    >>>def foo():
    >>>  return True
    >>>
    >>>wait_for_it_to.be_true(foo)
    >>>wait_for_it_to.be_true(foo, timeout=5)

    """
    start = time.time()
    while True:
        result = func()
        if result:
            return True
        if time.time() > start + timeout:
            msg = "expected something that evaluates to True, but got %s instead" % str(result)
            raise TimeoutError(msg)
        time.sleep(0.01)


def be_false(func, timeout=10):
    """
    waits until func evaluates to False
    raises an exception when the timeout expires

    :param timeout: a timeout in seconds
    :param func: an executable object

    >>>def foo():
    >>>  return False
    >>>
    >>>wait_for_it_to.be_false(foo)
    >>>wait_for_it_to.be_false(foo, timeout=5)
    """
    start = time.time()
    while True:
        result = func()
        if not result:
            return False
        if time.time() > start + timeout:
            msg = "expected something that evaluates to True, but got %s instead" % str(result)
            raise TimeoutError(msg)
        time.sleep(0.01)
