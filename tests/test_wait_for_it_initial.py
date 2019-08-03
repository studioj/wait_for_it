import unittest

from mock import patch, MagicMock

import wait_for_it


class TestWaitForItToBeTrue(unittest.TestCase):

    def test_wait_for_it_has_a_version(self):
        assert wait_for_it.__version__

    def test_wait_for_it_to_be_true_immediately_returns_when_func_evals_to_true(self):
        foo = MagicMock()
        foo.return_value = True
        with patch("wait_for_it.time.sleep") as mocked_sleep:
            wait_for_it.to_be_true(foo)
            mocked_sleep.assert_not_called()

    def test_to_be_true_sleeps_once_when_the_func_returns_only_after_the_second_try(self):
        foo = MagicMock()
        foo.side_effect = [False, True]
        with patch("wait_for_it.time.sleep") as mocked_sleep:
            wait_for_it.to_be_true(foo)
            mocked_sleep.assert_called_with(0.01)

    def test_to_be_true_calls_the_passed_function_obejct(self):
        foo = MagicMock()
        with patch("wait_for_it.time.sleep") as mocked_sleep:
            wait_for_it.to_be_true(foo)
            foo.assert_called_once()

    def test_to_be_true_raises_timeout_error_when_timeout_has_passed(self):
        foo = MagicMock()
        foo.return_value = False
        with patch("wait_for_it.time.sleep") as mocked_sleep:
            self.assertRaises(TimeoutError, wait_for_it.to_be_true, foo)
