

SELECT
    occupation_label,
    occupation_group,
    publication_date,
    application_deadline,
    duration_label
FROM "job_ads"."main"."stg_job_ads"
WHERE occupation_label IS NOT NULL