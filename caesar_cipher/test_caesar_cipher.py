import unittest
from caesar_cipher import caesarCipher

class TestCaesarCipher(unittest.TestCase):
    
    def test_give_middle_Outz_and_2_should_be_okffng_Qwvb(self):
        s = "middle-Outz"
        k = 2
        expected_output = "okffng-Qwvb"
        
        result = caesarCipher(s, k)
        
        self.assertEqual(result, expected_output)

    def test_give_abc_and_26_should_be_abc(self):
        s = "abc"
        k = 26
        expected_output = "abc"
        
        result = caesarCipher(s, k)
        
        self.assertEqual(result, expected_output)

    def test_give_symbols_should_remain_unchanged(self):
        s = "!@#-$%"
        k = 5
        expected_output = "!@#-$%"
        
        result = caesarCipher(s, k)
        
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()