
  
    
    

    create  table
      "job_ads"."main"."hospitality_mart__dbt_tmp"
  
    as (
      

SELECT *
FROM "job_ads"."main"."fct_job_ads"
WHERE occupation_group__label IN (
    'Hotell, restaurang, storhushåll',
    'Kockar och kallskänkor',
    'Hotellreceptionister m.fl.',
    'Restaurang- och köksbiträden m.fl.',
    'Hovmästare och servitörer',
    'Kafé- och konditoribiträden',
    'Pizzabagare m.fl.'
)
    );
  
  