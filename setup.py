#!/usr/bin/env python3
# -*- coding:utf-8 -*-


with open("README.md", "r") as fh:
        long_description = fh.read()


from setuptools import  setup, find_packages

setup(
    name="apkdownloader",
    version="0.0.1",
    keywords=("apk","apk download","download apk"),
    description="Download apk from Google Play via package name.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT Licence",
    url="https://github.com/krnick/apk-downloader",
    author="SONG,JUN-WEI",
    author_email="sungboss2004@gmail.com",
    packages=find_packages(),
    install_requires=[            
                'cryptography',
                'requests',
                'protobuf'
            ],
    classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
    ],
)
