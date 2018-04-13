# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 08:08:34 2018

@author: blk
"""

from setuptools  import setup, find_packages

setup(name="pywt",
      version="1.0.1",
      description="Python Webtrends connector",
      author="Bendik Knapstad",
      author_email="post@pinligstillhet.no",
      url="https://github.com/Knapstad/WT",
      py_modules=["wt"],
      install_requires=["requests", "typing", "json", "time", "os"],
      data_files=[("secrets/config.txt")],
      classifiers=[ 
      'Development Status :: 3 - Alpha',
      'License :: OSI Approved :: MIT License',
      'Programming Language :: Python :: 3'],
      packages=find_packages()

    )

    