

SELECT
  occupation_label AS occupation,
  COUNT(*) AS number_of_ads,
  duration_label,
  MIN(publication_date) AS earliest_publication,
  MAX(application_deadline) AS latest_deadline
FROM "job_ads"."main"."stg_job_ads"
WHERE occupation_group = 'Hotell, restaurang, storhushåll'
GROUP BY occupation_label, duration_label
ORDER BY number_of_ads DESC