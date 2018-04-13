# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 08:08:34 2018

@author: blk
"""

from distutils.core import setup

setup(name="WT",
      version="1.0",
      description="Python Webtrends connector",
      author="Bendik Knapstad",
      author_email="post@pinligstillhet.no",
      url=None,
      packages=["requests", "typing", "json", "time", "os"],
      data_files=[("seacrets/config.txt")])

    