
  
    
    

    create  table
      "job_ads"."main"."health_mart__dbt_tmp"
  
    as (
      

SELECT *
FROM "job_ads"."main"."fct_job_ads"
WHERE occupation_group__label = 'Hälso- och sjukvård'
    );
  
  