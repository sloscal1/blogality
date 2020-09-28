#!/usr/bin/env python

from distutils.core import setup

setup(
    name="blogality",
    version="0.1",
    description="Code to explore causality and related stuff.",
    author="Steven Loscalzo",
    author_email="sloscalzo85@gmail.com",
    url="https://github.com/sloscal1/blogality",
    packages=["blogality"],
    package_dir={'': 'src'},
    install_requires=[
        "numpy>=1.19.2",
    ],
)