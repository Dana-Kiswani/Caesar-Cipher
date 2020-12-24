from caesar_cipher import __version__
from caesar_cipher.caesar_cipher import *
import pytest


def test_version():
    assert __version__ == '0.1.0'

# [A.B.C.D.E.F.G.H.I.G.K.L.M.N.O.P.Q.R.S.T.U.V.W.X.Y.Z]

def test_encrypt() : 
    actual = encrypt('dana' , 1)
    expected = 'ebob'
    assert expected == actual


def test_decrypt() : 
    actual = decrypt('dana' , -4)
    expected = 'here'
    assert expected == actual


def test_encrypt_() : 
    actual = encrypt('blue bird' , -1)
    expected = 'aktd ahqc'
    assert expected == actual


def test_encrypt__() : 
    actual = encrypt('python' , 3)
    expected = 'sbwkrq'
    assert expected == actual