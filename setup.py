from setuptools import setup

from wait_for_it_to import __version__

version = __version__


longdesc = """
This is a library for letting you python code wait for a certain action top complete"""

setup(
    name="wait_for_it_to",
    version=version,
    description="helper library which waits",
    long_description=longdesc,
    author="Jef Neefs",
    author_email="neefsj@gmail.com",
    url="https://github.com/studioj/wait_for_it/",
    packages=["wait_for_it_to"],
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
