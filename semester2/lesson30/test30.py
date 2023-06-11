import unittest
import l30
 
class TestPlusFunction(unittest.TestCase):
    def setUp(self):
            print("Start to work a program")
    def test_plus(self): 
        test_num=10
        result=l30.plus(test_num)
        self.assertEqual(result,15)

    def test_plus_not_equal(self):
        test=10
        result=l30.plus(test)
        self.assertNotEqual(result,10)

    def test_plus_passing_string(self):
        test_val="a"
        result=l30.plus(test_val)
        self.assertIsInstance(result,ValueError)


    def test_plus_none_as_argument(self):
        test_num=None
        result=l30.plus(test_num)
        self.assertEqual(result,"please enter a number")

    def test_plus_without_arg(self):
        result=l30.plus()
        self.assertEqual(result,"please enter a number")

    def tearDown(self):
         print("Ending tests workflow")

if __name__=="__main__":
    unittest.main() 