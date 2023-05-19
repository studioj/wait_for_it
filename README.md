### waitforit

| What | Badges |
|------|--------|
| Code and Test Quality | [![codecov](https://codecov.io/gh/studioj/wait_for_it/branch/master/graph/badge.svg)](https://codecov.io/gh/studioj/wait_for_it) [![Codacy Badge](https://api.codacy.com/project/badge/Grade/d3292d34dbfd4fae8e2427da3bb77198)](https://www.codacy.com/manual/studioj/wait_for_it?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=studioj/wait_for_it&amp;utm_campaign=Badge_Grade) [![CodeFactor](https://www.codefactor.io/repository/github/studioj/wait_for_it/badge)](https://www.codefactor.io/repository/github/studioj/wait_for_it) |
| SonarQube | [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=studioj_wait_for_it&metric=alert_status)](https://sonarcloud.io/dashboard?id=studioj_wait_for_it) [![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=studioj_wait_for_it&metric=code_smells)](https://sonarcloud.io/dashboard?id=studioj_wait_for_it) [![Bugs](https://sonarcloud.io/api/project_badges/measure?project=studioj_wait_for_it&metric=bugs)](https://sonarcloud.io/dashboard?id=studioj_wait_for_it) [![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=studioj_wait_for_it&metric=vulnerabilities)](https://sonarcloud.io/dashboard?id=studioj_wait_for_it) |
| PyPI | ![PyPI - Downloads](https://img.shields.io/pypi/dw/wait_for_it_to?style=flat) |

This is a library for letting your python code wait for a certain action to complete

short example

Given these functions
```python
import wait_for_it_to
def foo():
  return True

def bar(param):
  x = param
  return False
```

This would immediatly return
```python
>> wait_for_it_to.be_true(foo)
>>
```

You can also pass parameters as a list
```python
>> wait_for_it_to.be_true(bar, args=[1])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "..\wait_for_it\wait_for_it_to\__init__.py", line 27, in be_true
    raise TimeoutError(msg)
TimeoutError: expected something that evaluates to True, but got False instead
```

You can also pass a timeout value in seconds
```python
>> wait_for_it_to.be_true(foo, timeout=5)
```
Quite similar you have the functionality
```python
>> wait_for_it_to.be_false(bar, timeout=5, args[1])
>> wait_for_it_to.equal(bar, False, timeout=5, args[1])
>> wait_for_it_to.not_raise_an_exception(bar, timeout=5, RuntimeError)
```
### Version History

<https://github.com/studioj/wait_for_it/releases>
