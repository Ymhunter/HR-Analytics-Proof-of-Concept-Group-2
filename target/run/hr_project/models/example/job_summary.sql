
  
    
    

    create  table
      "job_ads_pipeline"."main"."job_summary__dbt_tmp"
  
    as (
      

SELECT
  occupation_group__label AS occupation_group,
  COUNT(*) AS total_ads,
  MIN(publication_date) AS first_posted,
  MAX(publication_date) AS last_posted
FROM "job_ads_pipeline"."main"."stg_job_ads"
GROUP BY occupation_group__label
    );
  
  