import time
import unittest

from unittest.mock import MagicMock

import wait_for_it_to

EXCEPTION_STRING = "this keeps on failing"

try:
    a = TimeoutError()
except NameError:
    TimeoutError = wait_for_it_to.TimeoutError


class TestWaitForItToNotRaiseAnException(unittest.TestCase):
    def test_wait_for_it_not_to_raise_an_exception_returns_immediatly_when_no_exception_raised(
        self,
    ):
        func = MagicMock()

        start = time.time()
        wait_for_it_to.not_raise_an_exception(func)
        end = time.time()
        self.assertLessEqual(end - start, 0.01)

    def test_raises_a_timeout_error_when_func_keeps_raising_exceptions(self):
        def func():
            raise Exception(EXCEPTION_STRING)

        self.assertRaises(TimeoutError, wait_for_it_to.not_raise_an_exception, func, 1)

    def test_raises_a_timeout_error_when_func_keeps_raising_exceptions_which_are_equal_to_the_sentinel_exception(
        self,
    ):
        def func():
            raise RuntimeError(EXCEPTION_STRING)

        self.assertRaises(TimeoutError, wait_for_it_to.not_raise_an_exception, func, 1, RuntimeError)

    def test_raises_an_exception_which_is_not_equal_to_the_sentinel_exception(self):
        def func():
            raise RuntimeError(EXCEPTION_STRING)

        self.assertRaises(
            RuntimeError,
            wait_for_it_to.not_raise_an_exception,
            func,
            1,
            EnvironmentError,
        )

    def test_returns_if_succesfull(self):
        def func(num):
            return num

        self.assertEqual(5, wait_for_it_to.not_raise_an_exception(func, 1, Exception, args=[5]))
