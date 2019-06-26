import pytest
from fizzbuzz import *

def test_fizzbuzz_length():
    assert len(fizzbuzz()) == 100

def test_fizzbuzz_other_length():
    assert len(fizzbuzz(10)) == 10

def test_fizzbuzz_3():
    assert fizzbuzz()[2] == 'Fizz'
    assert fizzbuzz()[5] == 'Fizz'

def test_fizzbuzz_5():
    assert fizzbuzz()[4] == 'Buzz'
    assert fizzbuzz()[9] == 'Buzz'

def test_fizzbuzz_15():
    assert fizzbuzz()[14] == 'FizzBuzz'
    assert fizzbuzz()[29] == 'FizzBuzz'
