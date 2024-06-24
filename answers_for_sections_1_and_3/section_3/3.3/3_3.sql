--Give a breakdown of the number of genes for each chromosome.

SELECT CHROMOSOME, COUNT(*) FROM gene GROUP BY CHROMOSOME ORDER BY CHROMOSOME;