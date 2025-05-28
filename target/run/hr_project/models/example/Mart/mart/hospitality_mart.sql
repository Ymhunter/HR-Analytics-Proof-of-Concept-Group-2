
  
  create view "job_ads_pipeline"."main"."hospitality_mart__dbt_tmp" as (
    

SELECT
  occupation_group,
  occupation_label,
  COUNT(*) AS antal_annonser,
  MIN(publication_date) AS första_publicering,
  MAX(application_deadline) AS sista_ansökan
FROM "job_ads_pipeline"."main"."stg_job_ads"
WHERE occupation_group = 'Hotell, restaurang, storhushåll'
GROUP BY occupation_group, occupation_label
ORDER BY antal_annonser DESC
  );
