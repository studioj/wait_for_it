import unittest

from mock import patch, MagicMock

import wait_for_it_to


class TestWaitForItToBeFalse(unittest.TestCase):
    def test_wait_for_it_to_be_false_immediately_returns_when_func_evals_to_false(self):
        foo = MagicMock()
        foo.return_value = False
        with patch("wait_for_it_to.time.sleep") as mocked_sleep:
            wait_for_it_to.be_false(foo)
            mocked_sleep.assert_not_called()

    def test_to_be_false_sleeps_once_when_the_func_returns_only_after_the_second_try(self):
        foo = MagicMock()
        foo.side_effect = [True, False]
        with patch("wait_for_it_to.time.sleep") as mocked_sleep:
            wait_for_it_to.be_false(foo)
            mocked_sleep.assert_called_with(0.01)

    def test_to_be_false_calls_the_passed_function_obejct(self):
        foo = MagicMock(return_value=False)
        with patch("wait_for_it_to.time.sleep") as mocked_sleep:
            wait_for_it_to.be_false(foo)
            foo.assert_called_once()

    def test_to_be_true_raises_timeout_error_when_timeout_has_passed(self):
        foo = MagicMock(return_value=True)
        with patch("wait_for_it_to.time.sleep") as mocked_sleep:
            with patch("wait_for_it_to.time.time") as mocked_time:
                mocked_time.side_effect = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
                self.assertRaises(TimeoutError, wait_for_it_to.be_false, foo)

    def test_i_can_set_a_custom_timeout_for_to_be_false(self):
        foo = MagicMock(return_value=True)
        with patch("wait_for_it_to.time.sleep") as mocked_sleep:
            with patch("wait_for_it_to.time.time") as mocked_time:
                mocked_time.side_effect = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
                self.assertRaises(TimeoutError, wait_for_it_to.be_false, foo, 5)
                self.assertEqual(5, mocked_sleep.call_count)

    def test_default_timeout_for_to_be_false_is_10_seconds(self):
        foo = MagicMock(return_value=True)
        with patch("wait_for_it_to.time.sleep") as mocked_sleep:
            with patch("wait_for_it_to.time.time") as mocked_time:
                mocked_time.side_effect = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
                self.assertRaises(TimeoutError, wait_for_it_to.be_false, foo)
                self.assertEqual(10, mocked_sleep.call_count)
