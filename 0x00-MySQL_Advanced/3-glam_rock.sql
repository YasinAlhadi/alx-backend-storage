-- lists all bands with Glam rock as their main style.
SELECT band_name, (IFNULL(split, 2022) - formed) AS lifspan
FROM metal_bands
WHERE style LIKE '%Glam rock%' GROUP BY band_name , lifspan
ORDER BY lifspan DESC;
