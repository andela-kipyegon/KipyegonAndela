import unittest
from app.prime_generator import prime_number
class Tester(unittest.TestCase):
    def test_prime(self):
        self.assertEqual(prime_number(10),[2,3,5,7])
    def test_positive_numbers(self):
        self.assertEqual(prime_number(-20),'Only positive numbers')
    def test_string(self):
        self.assertEqual(prime_number("hello"),'Invalid Argument')
    def test_one(self):
        self.assertEqual(prime_number(1),[])
    def test_return_list(self):
        self.assertTrue(isinstance(prime_number(12),list))
    def test_list_length(self):
        self.assertEqual(len(prime_number(5)),3)
    def test_dict(self):
        self.assertEqual(prime_number({}),'Invalid Argument')
    def test_float(self):
        self.assertEqual(prime_number(3.2),'Invalid Argument')
    def test_list_argument(self):
        self.assertEqual(prime_number([1,2,3]),'Invalid Argument')
    def test_tuple(self):
        self.assertEqual(prime_number(()),'Invalid Argument')    
    
   
