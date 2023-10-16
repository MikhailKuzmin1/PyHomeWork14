from final import *
import unittest

class TestUnit(unittest.TestCase):
    def setUp(self):
        self.name = 'иван'
        self.value = '12368'
        self.secondvalue = 'a1b2c3'

    def test_count_num(self):
        self.assertRaises(ValueError, EmployeeID.__set__, self, self.name, self.value)

    def test_only_num(self):
        self.assertRaises(ValueError, EmployeeID.__set__, self, self.name, self.secondvalue)

    def test_title_name(self):
        self.assertRaises(ValueError, EmployeeName.__set__, self, self.value, self.name)
        

if __name__ == '__main__':
    unittest.main(verbosity=2)