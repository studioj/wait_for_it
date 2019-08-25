import time

from wait_for_it_to._version import __version__, __version_info__

try:
    a = TimeoutError()
except NameError:
    class TimeoutError(Exception):
        pass


def be_true(func, timeout=10):
    """
    waits until func returns True
    raises an exception when the timeout expires

    :param timeout: a timeout in seconds
    :param func: an executable object

    >>>def foo():
    >>>  return True
    >>>
    >>>wait_for_it_to.be_true(foo)
    >>>wait_for_it_to.be_true(foo, timeout=5)

    """
    be_equal(func, True, timeout)


def be_false(func, timeout=10):
    """
    waits until func returns False
    raises an exception when the timeout expires

    :param timeout: a timeout in seconds
    :param func: an executable object

    >>>def foo():
    >>>  return False
    >>>
    >>>wait_for_it_to.be_false(foo)
    >>>wait_for_it_to.be_false(foo, timeout=5)
    """
    be_equal(func, False, timeout)


def be_equal(func, expected_value, timeout=10):
    """
    waits until func is equal to expected_value
    raises an exception when the timeout expires

    :param expected_value: any value func should evaluate to
    :param timeout: a timeout in seconds
    :param func: an executable object

    >>>def foo():
    >>>  return "any object"
    >>>
    >>>wait_for_it_to.be_equal(foo, "any object")
    >>>wait_for_it_to.be_equal(foo, "any object", timeout=5)
    """
    start = time.time()
    result = func()
    while result != expected_value:
        if time.time() > start + timeout:
            msg = "expected something that evaluates to True, but got %s instead" % str(result)
            raise TimeoutError(msg)
        time.sleep(0.01)
        result = func()
