

SELECT
    duration_label,
    publication_date,
    application_deadline,
    working_hours AS working_hours_label
FROM "job_ads"."main"."stg_job_ads"
WHERE duration_label IS NOT NULL