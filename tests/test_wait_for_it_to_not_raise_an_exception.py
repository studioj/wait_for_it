import time
import unittest

import wait_for_it_to

try:
    a = TimeoutError()
except NameError:
    TimeoutError = wait_for_it_to.TimeoutError


class TestWaitForItToNotRaiseAnException(unittest.TestCase):
    def test_wait_for_it_not_to_raise_an_exception_returns_immediatly_when_no_exception_raised(self):
        def func():
            pass

        start = time.time()
        wait_for_it_to.not_raise_an_exception(func)
        end = time.time()
        self.assertLessEqual(end - start, 0.01)

    def test_raises_a_timeout_error_when_func_keeps_raising_exceptions(self):
        def func():
            raise Exception("this keeps on failing")

        self.assertRaises(TimeoutError, wait_for_it_to.not_raise_an_exception, func, 1)
