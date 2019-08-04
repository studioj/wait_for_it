import unittest

from mock import patch, MagicMock

import waitforit


class TestWaitForItToBeTrue(unittest.TestCase):

    def test_wait_for_it_has_a_version(self):
        assert waitforit.__version__

    def test_waitforit_to_be_true_immediately_returns_when_func_evals_to_true(self):
        foo = MagicMock()
        foo.return_value = True
        with patch("waitforit.time.sleep") as mocked_sleep:
            waitforit.to_be_true(foo)
            mocked_sleep.assert_not_called()

    def test_to_be_true_sleeps_once_when_the_func_returns_only_after_the_second_try(self):
        foo = MagicMock()
        foo.side_effect = [False, True]
        with patch("waitforit.time.sleep") as mocked_sleep:
            waitforit.to_be_true(foo)
            mocked_sleep.assert_called_with(0.01)

    def test_to_be_true_calls_the_passed_function_obejct(self):
        foo = MagicMock()
        with patch("waitforit.time.sleep") as mocked_sleep:
            waitforit.to_be_true(foo)
            foo.assert_called_once()

    def test_to_be_true_raises_timeout_error_when_timeout_has_passed(self):
        foo = MagicMock()
        foo.return_value = False
        with patch("waitforit.time.sleep") as mocked_sleep:
            self.assertRaises(TimeoutError, waitforit.to_be_true, foo)
