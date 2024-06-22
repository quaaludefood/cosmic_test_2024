from pathlib import Path
from utils import get_dataframe_from_file, get_mutations_from_dataframe, group_mutations_by_pattern
from datetime import datetime

def main():
    '''Main function to run the program.''' 
    input_file = Path('../simple_somatic_mutation.open.BLCA-CN.tsv')
    output_path = Path('../output_folder')

    if input_file.exists():
        dataframe = get_dataframe_from_file(input_file)
        #print(f'Dataframe generated: {dataframe}')
        mutations = get_mutations_from_dataframe(dataframe)
        patterns = group_mutations_by_pattern(mutations)
        #print(f'Patterns generated: {patterns}')
        for i in patterns.keys():
            print(patterns[i].BasepairChange, patterns[i].ICGCMutationId, patterns[i].Count)
        now = datetime.now()
        timestamp = int(now.timestamp())
        rows_file_name = f'rows_output_{timestamp}.txt'
       #generate_rows_file(rows_dict, output_path , rows_file_name)
        #print(f'Rows file generated: {rows_file_name}')


    else:
        raise ValueError("The file does not exist. Please check the path.")

if __name__ == "__main__":
    main()