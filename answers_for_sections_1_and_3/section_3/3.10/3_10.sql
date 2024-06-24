--If you want to make sure that all the id_gene ids in the transcript table 
--exists in the gene table, what kind of index would you create?

CREATE UNIQUE INDEX index_name ON transcript(id_gene);