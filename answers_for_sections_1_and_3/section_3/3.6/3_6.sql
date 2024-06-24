--List the Transcript accessions for the Gene Symbol AK1 with id_biotype 23 and flags gencode_basic

SELECT ACCESSION FROM transcript WHERE FLAGS = 'gencode_basic' AND ID_GENE = (SELECT ID_GENE FROM gene WHERE GENE_SYMBOL = 'AK1' AND ID_BIOTYPE = 23);