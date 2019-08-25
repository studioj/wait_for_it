import unittest

from mock import patch, MagicMock

import wait_for_it_to

try:
    a = TimeoutError()
except NameError:
    TimeoutError = wait_for_it_to.TimeoutError


class TestWaitForItToBeEqual(unittest.TestCase):
    def test_wait_for_it_to_be_equal_immediately_returns_when_func_evals_to_the_same_String(self):
        foo = MagicMock()
        foo.return_value = "some_value"
        with patch("wait_for_it_to.time.sleep") as mocked_sleep:
            wait_for_it_to.be_equal(foo, "some_value")
            mocked_sleep.assert_not_called()

    def test_to_be_equal_sleeps_once_when_the_func_returns_only_after_the_second_try(self):
        foo = MagicMock()
        foo.side_effect = [0, 1]
        with patch("wait_for_it_to.time.sleep") as mocked_sleep:
            wait_for_it_to.be_equal(foo, 1)
            mocked_sleep.assert_called_with(0.01)

    def test_to_be_equal_calls_the_passed_function_object(self):
        foo = MagicMock()
        foo.return_value = True
        with patch("wait_for_it_to.time.sleep") as mocked_sleep:
            wait_for_it_to.be_equal(foo, True)
            foo.assert_called_once()

    def test_to_be_equal_raises_timeout_error_when_timeout_has_passed(self):
        foo = MagicMock()
        foo.return_value = False
        with patch("wait_for_it_to.time.sleep") as mocked_sleep:
            with patch("wait_for_it_to.time.time") as mocked_time:
                mocked_time.side_effect = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
                self.assertRaises(TimeoutError, wait_for_it_to.be_equal, foo, True)

    def test_i_can_set_a_custom_timeout_for_to_be_equal(self):
        foo = MagicMock()
        foo.return_value = "False"
        with patch("wait_for_it_to.time.sleep") as mocked_sleep:
            with patch("wait_for_it_to.time.time") as mocked_time:
                mocked_time.side_effect = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
                self.assertRaises(TimeoutError, wait_for_it_to.be_equal, foo, "True", 5)
                self.assertEqual(5, mocked_sleep.call_count)

    def test_default_timeout_for_to_be_equal_is_10_seconds(self):
        foo = MagicMock()
        foo.return_value = False
        with patch("wait_for_it_to.time.sleep") as mocked_sleep:
            with patch("wait_for_it_to.time.time") as mocked_time:
                mocked_time.side_effect = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
                self.assertRaises(TimeoutError, wait_for_it_to.be_equal, foo, True)
                self.assertEqual(10, mocked_sleep.call_count)
