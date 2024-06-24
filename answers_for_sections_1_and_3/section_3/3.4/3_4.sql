--How many Transcripts does the Gene Symbol RAI14 has?

SELECT COUNT(*) FROM transcript WHERE ID_GENE = (SELECT ID_GENE FROM gene WHERE GENE_SYMBOL = 'RAI14');