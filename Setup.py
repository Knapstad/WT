# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 08:08:34 2018

@author: blk
"""

from setuptools  import setup, find_packages
import os
import json
def opj(*args):
    path = os.path.join(*args)
    return os.path.normpath(path)

def find_data_files(srcdir, *wildcards, **kw):
    # get a list of all files under the srcdir matching wildcards,
    # returned in a format to be used for install_data
    badnames=[".pyc","~","no_"]
def walk_helper(arg, dirname, files):
    if 'CVS' in dirname: ## ADD/CHANGE as you need here too.
        return
    names = []
    lst, wildcards = arg
    for wc in wildcards:
        wc_name = opj(dirname, wc)
        for f in files:
            filename = opj(dirname, f)
            #if ".pyc" not in filename:
            ## This hairy looking line excludes the filename
            ## if any part of one of  badnames is in it:
            if not any(bad in filename for bad in badnames):
                if fnmatch.fnmatch(filename, wc_name) and not os.path.isdir(filename):
                    names.append(filename)
    if names:
        lst.append( (dirname, names ) )

files = find_data_files('pywt/', '*.*')

setup(name="pywt",
      version="1.0.6",
      description="Python Webtrends connector",
      author="Bendik Knapstad",
      author_email="post@pinligstillhet.no",
      url="https://github.com/Knapstad/WT",
      py_modules=["pywt.wt"],
      install_requires=["requests"],
	  data_files=files,
      classifiers=[ 
      'Development Status :: 3 - Alpha',
      'License :: OSI Approved :: MIT License',
      'Programming Language :: Python :: 3'],
      packages=find_packages()

    )
if not os.path.exists("pywt/secrets"):
    os.makedirs("pywt/secrets")

config = {"proxies": None, "profile": None, "language": "en-GB", "format": "json", "auth": None, "verify": No

with open("pywt/secrets/config.txt", "w") as f:
	json.dump(config, f)