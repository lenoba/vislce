from distutils.core import setup
import py2exe, sys, os

sys.argv.append('py2exe')

setup(
    options = {'py2exe': {'includes':['Tkinter','ttk'],'bundle_files': 1, 'compressed': True}},
    windows = [{'script': "test.py"}],
    zipfile = None,
    dlls_in_exedir = [      "tcl85.dll",
                               "tk85.dll"]
)
