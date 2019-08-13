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
