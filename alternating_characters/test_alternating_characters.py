import unittest
from alternating_characters import alternatingCharacters

class TestAlternatingCharacters(unittest.TestCase):
    
    def test_give_AAAA_should_be_3(self):
        s = "AAAA"
        expected_output = 3
        
        result = alternatingCharacters(s)
        
        self.assertEqual(result, expected_output)

    def test_give_ABAB_should_be_0(self):
        s = "ABAB"
        expected_output = 0
        
        result = alternatingCharacters(s)
        
        self.assertEqual(result, expected_output)

    def test_give_AAABBB_should_be_4(self):
        s = "AAABBB"
        expected_output = 4
        
        result = alternatingCharacters(s)
        
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()