from os import path

from setuptools import setup

from wait_for_it_to import __version__

version = __version__

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()
with open('test_requirements.txt') as f:
    test_requirements = f.read().splitlines()

setup(
    name="wait_for_it_to",
    version=version,
    description="helper library which waits",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author="Jef Neefs",
    author_email="neefsj@gmail.com",
    url="https://github.com/studioj/wait_for_it/",
    packages=["wait_for_it_to"],
    tests_require=test_requirements,
    license="GPL",
    platforms="Posix; MacOS X; Windows",
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Topic :: Utilities",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
