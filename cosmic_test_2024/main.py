from pathlib import Path
from utils import get_dataframe_from_file, group_mutations
from datetime import datetime
import pandas as pd

def main():
    '''Main function to run the program.''' 
    input_file = Path('../simple_somatic_mutation.open.BLCA-CN.tsv')
    output_path = Path('../output_folder/output.tsv')

    if input_file.exists():
        pd.set_option('display.max_rows', 500)
        pd.set_option('display.max_columns', 500)
        pd.set_option('display.width', 150)
        dataframe = get_dataframe_from_file(input_file)
        grouped = group_mutations(dataframe)
        print(grouped)

    else:
        raise ValueError("The file does not exist. Please check the path.")

if __name__ == "__main__":
    main()