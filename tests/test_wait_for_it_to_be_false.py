import time
import unittest

from mock import MagicMock

import wait_for_it_to

try:
    a = TimeoutError()
except NameError:
    TimeoutError = wait_for_it_to.TimeoutError


class TestWaitForItToBeFalse(unittest.TestCase):
    def test_to_be_false_immediately_returns_when_func_evals_to_false(self):
        foo = MagicMock()
        foo.return_value = False

        start = time.time()
        wait_for_it_to.be_false(foo)
        self.assertLessEqual(time.time() - start, 0.002)

    def test_to_be_false_sleeps_once_when_the_func_returns_only_after_the_second_try(self):
        foo = MagicMock()
        foo.side_effect = [True, False]

        start = time.time()
        wait_for_it_to.be_false(foo)

        self.assertLessEqual(time.time() - start, 0.003)

    def test_to_be_false_calls_the_passed_function_obejct(self):
        foo = MagicMock(return_value=False)

        wait_for_it_to.be_false(foo)

        foo.assert_called_once()

    def test_to_be_false_raises_timeout_error_when_timeout_has_passed(self):
        foo = MagicMock(return_value=True)
        start = time.time()

        self.assertRaises(TimeoutError, wait_for_it_to.be_false, foo)
        self.assertLessEqual(time.time() - start, 10.1)

    def test_i_can_set_a_custom_timeout_for_to_be_false(self):
        foo = MagicMock(return_value=True)
        start = time.time()

        self.assertRaises(TimeoutError, wait_for_it_to.be_false, foo, 5)
        self.assertLessEqual(time.time() - start, 5.05)

    def test_default_timeout_for_to_be_false_is_10_seconds(self):
        foo = MagicMock(return_value=True)
        start = time.time()

        self.assertRaises(TimeoutError, wait_for_it_to.be_false, foo)
        self.assertLessEqual(time.time() - start, 10.1)

    def test_to_be_false_raises_timeout_error_when_func_returns_none(self):
        foo = MagicMock(return_value=None)
        start = time.time()

        self.assertRaises(TimeoutError, wait_for_it_to.be_true, foo, 5)
        self.assertLessEqual(time.time() - start, 5.05)

    def test_to_be_false_accepts_one_function_argument(self):
        def foo(an_argument):
            assert an_argument == the_argument
            return False

        the_argument = "the_argument"
        wait_for_it_to.be_false(foo, args=[the_argument])

    def test_to_be_false_accepts_two_function_arguments(self):
        the_argument = "the_argument"
        the_second_argument = "the_second_argument"

        def foo(an_argument, a_second_argument):
            assert an_argument == the_argument
            assert the_second_argument == a_second_argument
            return False

        wait_for_it_to.be_false(foo, args=[the_argument, the_second_argument])
