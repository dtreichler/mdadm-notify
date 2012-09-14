#!/bin/env python
# Filename: setup.py
# Created: Thu Sep 13 07:46:06 2012
# Created By: dtreichler
# Modified: Fri Sep 14 10:15:36 2012
# Modified By: dtreichler

from setuptools import setup

setup(
    name = "mdadm-notify",
    version = "0.1",
    author = "Derrick Treichler",
    description = ("A simple monitoring script for mdadm that emails outside ",
                   "addresses"),
    license = "BSD",
    scripts = [
        'mdadm-notify'
    ],
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "License :: OSI Approved :: BSD License",
        "Topic :: System :: Monitoring",
        "Operating System :: POSIX :: Linux",
    ],
)


