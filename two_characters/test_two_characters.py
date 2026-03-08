import unittest
from two_characters import alternate

class TestTwoCharacters(unittest.TestCase):
    
    def test_give_beabeefeab_should_be_5(self):
        s = "beabeefeab"
        expected_output = 5
        
        result = alternate(s)
        
        self.assertEqual(result, expected_output)

    def test_give_a_should_be_0(self):
        s = "a"
        expected_output = 0
        
        result = alternate(s)
        
        self.assertEqual(result, expected_output)

    def test_give_abaacdabd_should_be_4(self):
        s = "abaacdabd"
        expected_output = 4
        
        result = alternate(s)
        
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()