-- Script to list records with score >= 10 in second table
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC
