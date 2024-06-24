--List the Transcript accessions for the Gene Symbol AK1 with id_biotype 23 and flags gencode_basic

SELECT transcript_accession FROM transcript WHERE gene_id = 
(SELECT gene_id FROM gene WHERE gene_symbol = 'AK1' AND id_biotype = 23 AND flags = 'gencode_basic');