import time

from wait_for_it_to._version import __version__, __version_info__


def be_true(func):
    """
    waits until func evaluates to True
    raises an exception when the timeout expires

    :param func: an executable object
    
    >>>def foo():
    >>>  return True
    >>>
    >>>wait_for_it_to.be_true(foo)
    >>>
    
    """
    start = time.time()
    while True:
        result = func()
        if result:
            return
        if time.time() > start + 10:
            msg = "expected something that evaluates to True, but got %s instead" % str(result)
            raise TimeoutError(msg)
        time.sleep(0.01)
