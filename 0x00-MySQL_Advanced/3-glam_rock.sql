-- list all bands with Glam rock as their main style
SELECT band_name, COALESCE(split, 2020)-formed as "lifespan" FROM metal_bands
WHERE style LIKE '%Glam rock%'
GROUP BY band_name, lifespan
ORDER BY lifespan DESC;
