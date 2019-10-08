# assert 3>1,'你这是不正确的判断,第一个值不大于第二个值'

# age=input(">>>>")
# assert age.isdigit(),'%s不是数字'%age

import unittest
class OurTest(unittest.TestCase):
    def setUp(self):
        self.a=2
        self.b=2
    def test_equal(self):
        self.assertEqual(self.a,self.b)
    def test_equal(self):
        self.assertNotEqual(self.a,self.b)
    def tearDown(self):
        pass
if __name__=="__main__":
    unittest.main()





