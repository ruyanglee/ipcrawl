# coding=utf8

from distutils.core import setup  
import py2exe  

#extra_modules = ["bs4"]
options = {"py2exe":
                {"compressed": 1,
                 "optimize": 2,
                 "bundle_files": 1,
                 #"packages": extra_modules,
                 #"includes": extra_modules
                }
          }
setup(
    version = "1.0.0",
    description = "test for py2exe",
    name = "Py2exeTest",
    options = options,
    zipfile = None,
    console = [{"script": "app_main.py"}]
)
