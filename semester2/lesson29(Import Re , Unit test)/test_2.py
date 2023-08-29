import unittest
import h29
import random

x=random.randint(1,10)
class Test_find_num(unittest.TestCase):
    def test_find_num_passing_integer(self): 
        result=h29.find_num(5)
        self.assertTrue(result)

unittest.main()
        