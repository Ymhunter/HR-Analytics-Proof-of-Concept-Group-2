
  
  create view "job_ads_pipeline"."main"."stg_job_ads__dbt_tmp" as (
    with source as (SELECT *
FROM "job_ads_pipeline"."main"."job_ads_pipeline"

-- update schema if needed


),
flattened as (
    select
        id as job_id,
        headline.text as job_title,
        occupation.label as occupation,
        occupation_group.label as occupation_group,
        workplace_address.city as city,
        workplace_address.municipality as municipality,
        workplace_address.region as region,
        employment_type.label as employment_type,
        work_time_extent.label as work_time,
        description.text as job_description,
        employer.name as employer_name,
        publication_date,
        last_publication_date
    from source
)

select * from flattened
  );
