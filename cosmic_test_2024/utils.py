
import pandas as pd
from pandas import DataFrame


def get_dataframe_from_file(file_path):
    '''Reads a file and returns a pandas DataFrame.'''
    try:
        df = pd.read_csv(file_path, sep='\t')
    except:
        raise ValueError("The file could not be read. Please check the format.")
    return df

def group_mutations(dataframe):
    '''Groups mutations by mutated_from_allele, mutated_to_allele and icgc_mutation_id.'''
    grouped = dataframe.groupby(['mutated_from_allele', 'mutated_to_allele'])['icgc_mutation_id'].count()
    return grouped


