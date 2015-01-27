#!/usr/bin/env python
#-*- coding:utf-8 -*-

try:
    import curve25519
    ext_modules = [curve25519.ffi.verifier.get_extension()]
except:
    ext_modules = []
    from traceback import print_exc
    print_exc()

from distutils.core import setup, Extension

setup (name = 'pycurve25519',
       version = '1.1',
       url = 'https://github.com/TomCrypto/pycurve25519',
       license = 'BSD',
       description = 'Python wrapper for curve25519',
       author = 'Thomas BENETEAU',
       author_email = 'thomas.beneteau@yahoo.fr',
       packages = ['curve25519'],
       ext_package = 'curve25519',
       ext_modules = ext_modules,
       install_requires = ['cffi'],
       requires = ['cffi'])
