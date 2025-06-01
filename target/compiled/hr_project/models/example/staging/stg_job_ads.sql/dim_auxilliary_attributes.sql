

SELECT
    id,
    duration_label,
    publication_date,
    working_hours,
    application_deadline
FROM "job_ads"."main"."stg_job_ads"
WHERE id IS NOT NULL