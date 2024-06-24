--Imagine that we have a table called “some_gene” with only a subset of the gene data. 
--If I want to join the gene table with this table but display all the genes in the result, 
--what kind of join would you do?


--Left Join would retrieve all the records on the left taable (gene) in this case and the matched records from the right table (some_gene).
--Example:

SELECT * FROM gene LEFT JOIN some_gene ON gene.ID_GENE = some_gene.ID_GENE;