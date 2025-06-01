
  
    
    

    create  table
      "job_ads"."main"."fct_job_ads__dbt_tmp"
  
    as (
      

SELECT
    id,
    occupation_label,
    duration_label,
    publication_date,
    application_deadline,
    working_hours,
    region
FROM "job_ads"."main"."stg_job_ads"
WHERE occupation_label IS NOT NULL
    );
  
  