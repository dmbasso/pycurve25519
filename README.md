pycurve25519
============

Python wrapper for curve25519 (based on [curve25519-donna](https://code.google.com/p/curve25519-donna/)).

Tested on Python 2.7, Python 3.3, and PyPy 2.4. Note: it is around 3 orders of
magnitude *slower* than the equivalent functions in PyNaCl.

Usage
-----

    import curve25519
    
    # Generate two private keys
    privateA = curve25519.genkey()
    privateB = curve25519.genkey()
    
    # Obtain the equivalent public keys
    publicA = curve25519.public(privateA)
    publicB = curve25519.public(privateB)
    
    # Compute the shared secret (sharedA == sharedB)
    sharedA = curve25519.shared(privateA, publicB)
    sharedB = curve25519.shared(privateB, publicA)
    
    # Pass the shared secret in a KDF or other before use

Installation
------------

You need `pip` and the development headers of Python and the Foreign Function
Interface library. On a Debian-derived OS you can `apt-get install python-pip
python-dev libffi-dev`.

    pip install -r requirements.txt
    python setup.py install
    python test_curve25519.py
