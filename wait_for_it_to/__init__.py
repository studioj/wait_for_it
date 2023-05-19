import time
from threading import Event, Thread

from wait_for_it_to._version import __version__, __version_info__

try:
    a = TimeoutError()
except NameError:

    class TimeoutError(Exception):
        pass


class Waiter(object):
    def __init__(self):
        self.timeout_timer = None
        self.args = []
        self.kwargs = {}
        self.finished = Event()

    def cancel(self, time_out):
        """Stop the timer if it hasn't finished yet."""
        for _ in range(time_out * 10):
            if self.finished.is_set():
                return
            time.sleep(0.1)
        self.finished.set()

    def wait_for_it_to_be_equal(self, timeout, function, expected_value, args=None, kwargs=None):
        self._prepare_for_waiting(args, kwargs, timeout)
        while not self.finished.is_set():
            result = function(*self.args, **self.kwargs)
            if result == expected_value:
                self.finished.set()
                return result
            time.sleep(0.001)
        raise TimeoutError()

    def wait_for_it_to_not_raise_an_exception(self, function, timeout, sentinel_exception, args=None, kwargs=None):
        self._prepare_for_waiting(args, kwargs, timeout)
        while not self.finished.is_set():
            try:
                return function(*self.args, **self.kwargs)
            except sentinel_exception:
                pass
            time.sleep(0.001)
        raise TimeoutError()

    def _prepare_for_waiting(self, args, kwargs, timeout):
        self.finished.clear()
        self.timeout_timer = Thread(target=self.cancel, args=(timeout,))
        self.args = args if args is not None else []
        self.kwargs = kwargs if kwargs is not None else {}
        self.timeout_timer.start()


def be_true(func, timeout=10, args=None, kwargs=None):
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
    be_equal(func, True, timeout, args=args, kwargs=kwargs)


def be_false(func, timeout=10, args=None, kwargs=None):
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
    be_equal(func, False, timeout, args=args, kwargs=kwargs)


def be_equal(func, expected_value, timeout=10, args=None, kwargs=None):
    """
    waits until func is equal to expected_value
    raises an exception when the timeout expires

    :param func_args: argument list
    :param expected_value: any value func should evaluate to
    :param timeout: a timeout in seconds
    :param func: an executable object

    >>>def foo():
    >>>  return "any object"
    >>>
    >>>wait_for_it_to.be_equal(foo, "any object")
    >>>wait_for_it_to.be_equal(foo, "any object", timeout=5)
    """
    waiter = Waiter()
    waiter.wait_for_it_to_be_equal(timeout, func, expected_value, args, kwargs)


def not_raise_an_exception(func, timeout=10, sentinel_exception=Exception, args=None, kwargs=None):
    waiter = Waiter()
    return waiter.wait_for_it_to_not_raise_an_exception(func, timeout, sentinel_exception, args, kwargs)
