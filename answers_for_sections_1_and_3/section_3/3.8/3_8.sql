--Imagine that the gene and transcript tables are getting very big and that 
--joining the two tables get slower and slower. What would you do to improve performances?

--Create an index on the ID_GENE column in the transcript table.
--Also views specific for each use case which only contain a subset of the columns or rows needed.
