from mock import patch

import wait_for_it


def test_wait_for_it_has_a_version():
    assert wait_for_it.__version__


def test_wait_for_it_to_be_true_immediately_returns_when_func_evals_to_true():
    def foo():
        return True

    with patch("wait_for_it.time.sleep") as mocked_sleep:
        wait_for_it.to_be_true(foo)
        mocked_sleep.assert_not_called()
