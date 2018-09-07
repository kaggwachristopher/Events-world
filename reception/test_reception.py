import unittest
from reception1.reception import Reception

class reception_test(unittest.TestCase):
    def setUp(self):
        self.ordinary_name="chris"
        self.vip_name="joseph"
        self.tester=Reception()
    def tearDown(self):
        pass
    def test_ordinary_checker(self):
        self.assertEquals (self.tester.registration_checker(self.ordinary_name),"Christopher Kaggwa ordinary")
    def test_vip_checker(self):
        self.assertEquals (self.tester.registration_checker(self.vip_name),"kasule joseph VIP")
    def test_validation(self):
           with self.assertRaises(TypeError):
                self.tester.validation(" ")
    def test_init(self):
        self.assertEquals(self.tester.__init__(),None)
    def test_function_checker(self):
        self.assertEquals(self.tester.check_function(),True)
        


