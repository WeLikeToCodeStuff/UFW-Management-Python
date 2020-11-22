import os
from setuptools import setup, find_packages

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="ufw-config",
    version="0.0.4",
    author="WeLikeToCodeStuff",
    description=("Configure UFW"),
    license="Apache 2.0",
    keywords="ufw configuration tool",
    url="https://github.com/WeLikeToCodeStuff/UFW-Management-Python",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            ""
        ],
    },
    long_description=read('README.md'),
    long_description_content_type="text/markdown",
    classifiers=[
        "Topic :: Utilities",
    ],
)
