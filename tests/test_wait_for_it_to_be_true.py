import time
import unittest

from mock import MagicMock

import wait_for_it_to

try:
    a = TimeoutError()
except NameError:
    TimeoutError = wait_for_it_to.TimeoutError


class TestWaitForItToBeTrue(unittest.TestCase):
    def test_wait_for_it_to_has_a_version(self):
        assert wait_for_it_to.__version__

    def test_wait_for_it_to_to_be_true_immediately_returns_when_func_evals_to_true(self):
        foo = MagicMock()
        foo.return_value = True

        start = time.time()
        wait_for_it_to.be_true(foo)

        self.assertLessEqual(time.time() - start, 0.001)

    def test_to_be_true_sleeps_once_when_the_func_returns_only_after_the_second_try(self):
        foo = MagicMock()
        foo.side_effect = [True, False]

        start = time.time()
        wait_for_it_to.be_true(foo)

        self.assertLessEqual(time.time() - start, 0.002)

    def test_to_be_true_calls_the_passed_function_object(self):
        foo = MagicMock()
        foo.return_value = True

        wait_for_it_to.be_true(foo)

        foo.assert_called_once()

    def test_to_be_true_raises_timeout_error_when_timeout_has_passed(self):
        foo = MagicMock(return_value=False)
        start = time.time()

        self.assertRaises(TimeoutError, wait_for_it_to.be_true, foo)

        self.assertLessEqual(time.time() - start, 10.1)

    def test_i_can_set_a_custom_timeout_for_to_be_true(self):
        foo = MagicMock(return_value=False)
        start = time.time()

        self.assertRaises(TimeoutError, wait_for_it_to.be_true, foo, 5)
        self.assertLessEqual(time.time() - start, 5.05)

    def test_default_timeout_for_to_be_true_is_10_seconds(self):
        foo = MagicMock(return_value=False)
        start = time.time()

        self.assertRaises(TimeoutError, wait_for_it_to.be_true, foo)
        self.assertLessEqual(time.time() - start, 10.1)

    def test_to_be_true_raises_timeout_error_when_func_returns_a_string(self):
        foo = MagicMock(return_value="a string which isnt equal to True")
        start = time.time()

        self.assertRaises(TimeoutError, wait_for_it_to.be_true, foo, 5)
        self.assertLessEqual(time.time() - start, 5.05)

    def test_to_be_true_accepts_one_function_argument(self):
        def foo(an_argument):
            assert an_argument == the_argument
            return True

        the_argument = "the_argument"
        wait_for_it_to.be_true(foo, args=[the_argument])

    def test_to_be_true_accepts_two_function_arguments(self):
        the_argument = "the_argument"
        the_second_argument = "the_second_argument"

        def foo(an_argument, a_second_argument):
            assert an_argument == the_argument
            assert the_second_argument == a_second_argument
            return True

        wait_for_it_to.be_true(foo, args=[the_argument, the_second_argument])
