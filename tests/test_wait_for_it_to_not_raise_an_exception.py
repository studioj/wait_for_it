import time
import unittest

from mock import MagicMock

import wait_for_it_to

try:
    a = TimeoutError()
except NameError:
    TimeoutError = wait_for_it_to.TimeoutError


class TestWaitForItToNotRaiseAnException(unittest.TestCase):
    def test_wait_for_it_not_to_raise_an_exception_returns_immediatly_when_no_exception_raised(self):
        func = MagicMock()

        start = time.time()
        wait_for_it_to.not_to_raise_an_exception(func)
        end = time.time()
        self.assertLessEqual(end - start, 0.01)
