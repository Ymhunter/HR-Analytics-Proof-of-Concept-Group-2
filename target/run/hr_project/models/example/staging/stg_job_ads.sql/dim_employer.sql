
  
    
    

    create  table
      "job_ads"."main"."dim_employer__dbt_tmp"
  
    as (
      

SELECT
    employer_name,
    employer_url,
    employer__organization_number
FROM "job_ads"."main"."stg_job_ads"
WHERE employer_name IS NOT NULL
    );
  
  