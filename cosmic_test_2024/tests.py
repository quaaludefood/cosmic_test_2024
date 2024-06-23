import unittest
from utils import get_dataframe_from_file, group_mutations
import pandas as pd

class TestDataFrameFromFile(unittest.TestCase):
    def test_valid_file(self):
        '''Test with a valid file'''
        file_path = '../simple_somatic_mutation.open.BLCA-CN.tsv'
        df = get_dataframe_from_file(file_path)
        self.assertIsInstance(df, pd.DataFrame)
    
    def test_invalid_file(self):
        '''Test with a non-existent file'''
        file_path = '/path/to/invalid/file.tsv'
        with self.assertRaises(ValueError):
            get_dataframe_from_file(file_path)

    def test_group_mutations(self):
        '''Create a sample dataframe for testing'''
        data = {
            'mutated_from_allele': ['A', 'A', 'C', 'C', 'G'],
            'mutated_to_allele': ['T', 'T', 'G', 'G', 'A'],
            'icgc_mutation_id': ['abc', 'abc', 'def', 'ghi', 'jkl']
        }
        df = pd.DataFrame(data)
        result = group_mutations(df)
        expected = pd.Series([2, 2,1], index=[('A', 'T'), ('C', 'G'), ('G', 'A')])

        self.assertTrue(result.equals(expected))

if __name__ == '__main__':
    unittest.main()