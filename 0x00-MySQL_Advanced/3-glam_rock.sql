-- list all bands with Glam rock as their main style
SELECT band_name, (IFNULL(split, YEAR(NOW())) - formed) AS lifespan
FROM metal_bands
WHERE FIND_IN_SET('Glam rock', CONCAT_WS("", style)) > 0
ORDER BY lifespan DESC;
