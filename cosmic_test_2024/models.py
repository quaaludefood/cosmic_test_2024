class Mutation():
    '''Class to represent a region.'''
    MutatedFromAllele: str
    MutatedToAllele: str
    ICGCMutationId: str

    def __init__(self, mutated_from_allele, mutated_to_allele, icgc_mutation_id):
        self.MutatedFromAllele = mutated_from_allele
        self.MutatedToAllele = mutated_to_allele
        self.ICGCMutationId = icgc_mutation_id

class Pattern():
    '''Class to represent a pattern.'''
    BasepairChange: str
    ICGCMutationId: str
    Count: int  

    def __init__(self, basepair_change, icgc_mutation_id, count):
        self.BasepairChange = basepair_change
        self.ICGCMutationId = icgc_mutation_id
        self.Count = count

