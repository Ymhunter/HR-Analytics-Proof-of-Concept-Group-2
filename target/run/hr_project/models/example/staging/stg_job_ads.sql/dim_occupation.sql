
  
    
    

    create  table
      "job_ads"."main"."dim_occupation__dbt_tmp"
  
    as (
      

SELECT
    id,
    occupation_group__label,
    occupation_label,
    publication_date,
    employer__organization_number,
    working_hours
FROM "job_ads"."main"."stg_job_ads"
WHERE id IS NOT NULL
    );
  
  