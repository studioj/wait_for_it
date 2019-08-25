# waitforit
### Badges
##### Travis Build
[![Build Status](https://travis-ci.com/studioj/wait_for_it.svg?branch=master)](https://travis-ci.com/studioj/wait_for_it)

##### Code and Test Quality
[![codecov](https://codecov.io/gh/studioj/wait_for_it/branch/master/graph/badge.svg)](https://codecov.io/gh/studioj/wait_for_it)
[![BCH compliance](https://bettercodehub.com/edge/badge/studioj/wait_for_it?branch=master)](https://bettercodehub.com/)
[![CodeFactor](https://www.codefactor.io/repository/github/studioj/wait_for_it/badge)](https://www.codefactor.io/repository/github/studioj/wait_for_it)

##### SonarQube
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=studioj_wait_for_it&metric=alert_status)](https://sonarcloud.io/dashboard?id=studioj_wait_for_it)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=studioj_wait_for_it&metric=code_smells)](https://sonarcloud.io/dashboard?id=studioj_wait_for_it)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=studioj_wait_for_it&metric=bugs)](https://sonarcloud.io/dashboard?id=studioj_wait_for_it)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=studioj_wait_for_it&metric=vulnerabilities)](https://sonarcloud.io/dashboard?id=studioj_wait_for_it)

##### PyPI

![PyPI - Downloads](https://img.shields.io/pypi/dw/wait_for_it_to?style=flat)

This is a library for letting your python code wait for a certain action to complete

short example

```python
import wait_for_it_to
def foo():
  return True

def bar():
  return False
  
>> wait_for_it_to.be_true(foo)

>> wait_for_it_to.be_true(bar)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "..\wait_for_it\wait_for_it_to\__init__.py", line 27, in be_true
    raise TimeoutError(msg)
TimeoutError: expected something that evaluates to True, but got False instead

>> wait_for_it_to.be_true(foo, timeout=5)
```
#### Version History

https://github.com/studioj/wait_for_it/releases