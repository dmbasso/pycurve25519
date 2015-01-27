#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""Python wrapper for curve25519."""

from os import urandom
from cffi import FFI


ffi = FFI()

ffi.cdef("""
    void curve25519_donna(char *pub, const char *priv, const char *basepoint);
""")

_lib = ffi.verify(sources=["curve25519/curve25519-donna.c"],
                  ext_package="curve25519",
                  extra_compile_args=["-O3"])

base_pt = b'\x09' + 31 * b'\0'


def genkey():
    key = bytearray(urandom(32))
    key[0] &= 248
    key[31] &= 127
    key[31] |= 64
    return bytes(key)


def public(private):
    key = ffi.new("char [32]")
    _lib.curve25519_donna(key, private, base_pt)
    return bytes(ffi.buffer(key))


def shared(private, public):
    key = ffi.new("char [32]")
    _lib.curve25519_donna(key, private, public)
    return bytes(ffi.buffer(key))


__all__ = ["genkey", "public", "shared", "ffi"]
