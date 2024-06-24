--What is the canonical transcript accession for Ensembl Gene id ENSG00000266960?

SELECT ACCESSION FROM transcript WHERE ID_GENE = (SELECT ID_GENE FROM gene WHERE ENSEMBL_GENE_ID = 'ENSG00000266960');