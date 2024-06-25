--If you want to make sure that all the id_gene ids in the transcript table 
--exists in the gene table, what kind of index would you create?

--Create a unique index on the id_gene column in the transcript table, e.g:

CREATE UNIQUE INDEX index_name ON transcript(id_gene);