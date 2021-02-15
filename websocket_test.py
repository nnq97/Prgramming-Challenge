#!/usr/bin/env python
#
# This test script is used to test the functions when user replace hardcore input
#
from websocket_lsg import *


def test_method1():
    # Test to pass every data type check
    assert check_int(1123) == True
    assert check_str("Testing") == True
    assert check_file("another.json") == True


def test_method2():
    # Test to fail - str not equal to int
    assert check_int("he") == True


def test_method3():
    # Test to fail - differentiating between filename and regular string input
    assert check_file("he") == True


def test_method4():
    # Test to fail - file does not exist
    assert check_file('hey.json') == True


def test_method5():
    # Test to pass - file does not exist
    assert check_file('hey.json') == False


def test_method6():
    try:
        # Test to pass - send data and echo back from server
        connection()
    finally:
        assert send_int(1142) == "1142"
        assert send_str("Hi") == "Hi"
        assert send_json("data.json") == "{'id': 'c-1', 'type': 'compressor'}"


def test_method7():
    try:
        # Test to fail - send data and echo back from server
        connection()
    finally:
        assert send_str("Hello") == "Hi"
