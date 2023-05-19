import time
import unittest

from unittest.mock import patch, MagicMock

import wait_for_it_to

try:
    a = TimeoutError()
except NameError:
    TimeoutError = wait_for_it_to.TimeoutError


class TestWaitForItToBeEqual(unittest.TestCase):
    def test_to_be_equal_sleeps_once_when_the_func_returns_only_after_the_second_try(
        self,
    ):
        foo = MagicMock()
        foo.side_effect = [0, 1]
        wait_for_it_to.be_equal(foo, 1)
        self.assertEqual(2, foo.call_count)

    def test_to_be_equal_raises_timeout_error_when_timeout_has_passed(self):
        foo = MagicMock()
        foo.return_value = False
        with patch("wait_for_it_to.time.sleep"):
            with patch("wait_for_it_to.time.time") as mocked_time:
                mocked_time.side_effect = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
                self.assertRaises(TimeoutError, wait_for_it_to.be_equal, foo, True)

    def test_i_can_set_a_custom_timeout_for_to_be_equal_which_drifts_only_10_percent(
        self,
    ):
        def foo():
            return False

        start = time.time()
        self.assertRaises(TimeoutError, wait_for_it_to.be_equal, foo, "True", 5)
        self.assertLessEqual(time.time() - start, 5.1)

    def test_default_timeout_for_to_be_equal_is_lower_than_10_1_seconds(self):
        def foo():
            return False

        start = time.time()
        self.assertRaises(TimeoutError, wait_for_it_to.be_equal, foo, True)
        self.assertLessEqual(time.time() - start, 10.1)

    def test_to_be_equal_raises_an_exception_if_params_is_not_a_list(self):
        def foo(an_argument):
            if an_argument != the_argument:
                raise AssertionError()
            return True

        the_argument = "the_argument"
        self.assertRaises(TypeError, lambda: wait_for_it_to.be_equal(foo, True, args=the_argument))

        the_argument = 1
        self.assertRaises(TypeError, lambda: wait_for_it_to.be_equal(foo, True, args=the_argument))


def test_to_be_equal_accepts_one_function_argument():
    def foo(an_argument):
        if an_argument != the_argument:
            raise AssertionError()
        return True

    the_argument = "the_argument"
    wait_for_it_to.be_equal(foo, True, 2, [the_argument])


def test_to_be_equal_accepts_two_function_arguments():
    the_argument = "the_argument"
    the_second_argument = "the_second_argument"

    def foo(an_argument, a_second_argument):
        if an_argument != the_argument:
            raise AssertionError()
        if the_second_argument != a_second_argument:
            raise AssertionError()
        return True

    wait_for_it_to.be_equal(foo, True, args=[the_argument, the_second_argument])


def test_wait_for_it_to_be_equal_immediately_returns_when_func_evals_to_the_same_string():
    foo = MagicMock(return_value="some_value")
    wait_for_it_to.be_equal(foo, "some_value")
    foo.assert_called_once()


def test_to_be_equal_calls_the_passed_function_object():
    foo = MagicMock()
    foo.return_value = True

    wait_for_it_to.be_equal(foo, True)
    foo.assert_called_once()
