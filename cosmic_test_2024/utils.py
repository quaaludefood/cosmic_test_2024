from models import Mutation
import pandas as pd
from pandas import DataFrame


def get_dataframe_from_file(file_path):
    '''Reads a file with regions and returns a list of Region objects.'''
    try:
        df = pd.read_csv(file_path, sep='\t')
    except:
        raise ValueError("The file could not be read. Please check the format.")
    return df

def get_mutations_from_dataframe(dataframe):
    '''Returns a list of Mutation objects from a dataframe.'''
    mutations = []
    for index, row in dataframe.iterrows():
        mutation = Mutation(row['mutated_from_allele'], row['mutated_to_allele'], row['icgc_mutation_id'])
        #print(mutation)
        mutations.append(mutation)
    return mutations

def create_dict_of_patterns(mutations):
    '''Groups mutations by pattern.'''
    patterns_dict = {}
    for mutation in mutations:
        icgc_mutation_id = mutation.ICGCMutationId
        mutated_to_dict = {mutation.MutatedFromAllele: [icgc_mutation_id]}
        if mutation.MutatedFromAllele not in patterns_dict:
            patterns_dict[mutation.MutatedFromAllele] = mutated_to_dict
        else:
            mutated_from_dict = patterns_dict[mutation.MutatedFromAllele]
            if mutation.MutatedToAllele not in mutated_from_dict:
                mutated_from_dict[mutation.MutatedToAllele] = [icgc_mutation_id]
            else:
                patterns_dict[mutation.MutatedFromAllele][mutation.MutatedToAllele].append(icgc_mutation_id)
    return patterns_dict



def generate_rows_file(rows_dict, output_path, file_name):
    '''Generates a file with the regions assigned to rows.'''
    with open(str(output_path) + '/' + file_name, 'w') as file:
        for row in rows_dict.keys():
            for region in rows_dict[row]:
                file.write(f"{row}\t{region.Start}\t{region.End}\n")


    


