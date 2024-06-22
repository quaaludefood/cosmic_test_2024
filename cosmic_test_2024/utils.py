from models import Mutation
import pandas as pd
from pandas import DataFrame


def get_dataframe_from_file(file_path):
    '''Reads a file with regions and returns a list of Region objects.'''
    mutations = []

    try:
        df = pd.read_csv(file_path, sep='\t')
    except:
        raise ValueError("The file could not be read. Please check the format.")
    return df

def generate_rows_file(rows_dict, output_path, file_name):
    '''Generates a file with the regions assigned to rows.'''
    with open(str(output_path) + '/' + file_name, 'w') as file:
        for row in rows_dict.keys():
            for region in rows_dict[row]:
                file.write(f"{row}\t{region.Start}\t{region.End}\n")


    


