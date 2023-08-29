import unittest
import l29
 
class TestPlusFunction(unittest.TestCase):
    def setUp(self):
            print("Start to work a program")
    def test_plus(self): 
        test_num=10
        result=l29.plus(test_num)
        self.assertEqual(result,15)

    def test_plus_not_equal(self):
        test=10
        result=l29.plus(test)
        self.assertNotEqual(result,10)

    def test_plus_passing_string(self):
        test_val="a"
        result=l29.plus(test_val)
        self.assertIsInstance(result,ValueError)

unittest.main()