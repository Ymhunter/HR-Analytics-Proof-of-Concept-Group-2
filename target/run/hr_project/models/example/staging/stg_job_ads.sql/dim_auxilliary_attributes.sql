
  
    
    

    create  table
      "job_ads"."main"."dim_auxilliary_attributes__dbt_tmp"
  
    as (
      

SELECT
    id,
    duration_label,
    publication_date,
    working_hours,
    application_deadline
FROM "job_ads"."main"."stg_job_ads"
WHERE id IS NOT NULL
    );
  
  