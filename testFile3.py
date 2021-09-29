#testFile.py

from lab03 import *

def test_power():
    assert power(3,3) == 27
    assert power(10,0) == 1
    assert power(0,10) == 0

def test_integerdiv():
    assert integerDivision(101,10) == 10
    assert integerDivision(0,1) == 0
    assert integerDivision(20,3) == 6
    assert integerDivision(30,1) == 30
    
def test_collectVowels():
    x = "I want to learn how to code"
    y = ""
    z = "XXXXXX:'i'kdj"
    assert collectVowels(x) == ['I','a','o','e','a','o','o','o','e']
    assert collectVowels(y) == []
    assert collectVowels(z) == ['i']
    
def test_reverseString():
    x = "Racecar"
    y = "x"
    z = "robber"
    assert reverseString(x) == "racecaR"
    assert reverseString(y) == "x"
    assert reverseString(z) == "rebbor"
    
def test_removeSubString():
    x = "bubble butt"
    y = "on top, or on the bottom?"
    z = "Rose: flower:"
    assert removeSubString(x,"b") == "ule utt"
    assert removeSubString(y,"on") == " top, or  the bottom?"
    assert removeSubString(z,":") == "Rose flower"