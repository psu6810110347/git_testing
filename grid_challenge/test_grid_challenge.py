import unittest
from grid_challenge import gridChallenge

class TestGridChallenge(unittest.TestCase):
    
    def test_give_valid_grid_should_be_YES(self):
        grid = ['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv']
        expected_output = "YES"
        
        result = gridChallenge(grid)
        
        self.assertEqual(result, expected_output)

    def test_give_invalid_grid_should_be_NO(self):
        grid = ['mpxz', 'abcd', 'wlmf']
        expected_output = "NO"
        
        result = gridChallenge(grid)
        
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()