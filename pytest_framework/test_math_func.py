import unittest

from Learnings import math_func

class Test_math_func(unittest.TestCase):

    def test_add(self):    # test_function name from your .py for which function you want to write the test cases.
        assert math_func.add(2, 3) == 5     # asserting that the function is returning the desired result.
        assert  math_func.add(4) == 6

    def test_product(self):
        assert math_func.product(5, 10) == 50
        assert math_func.product(4) == 8

    def test_add_strings(self):
        result = math_func.add('ab', 'cd')
        assert result == 'abcd'
        assert type(result) is str
        assert 'abcd' in result
        assert 'ghjk' not in result
