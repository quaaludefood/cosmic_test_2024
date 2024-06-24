--How many Transcripts does the Gene Symbol RAI14 has?

SELECT COUNT(*) FROM transcript WHERE gene_id = (SELECT gene_id FROM gene WHERE gene_symbol = 'RAI14');