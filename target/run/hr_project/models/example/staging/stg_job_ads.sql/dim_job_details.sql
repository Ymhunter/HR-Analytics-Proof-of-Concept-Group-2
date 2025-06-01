
  
    
    

    create  table
      "job_ads"."main"."dim_job_details__dbt_tmp"
  
    as (
      

SELECT
    id,
    headline,
    description_text,
    application_deadline,
    publication_date,
    occupation_label
FROM "job_ads"."main"."stg_job_ads"
WHERE id IS NOT NULL
    );
  
  