

SELECT
    id,
    headline,
    employer_name AS employer_name,
    workplace_address__region AS region,
    occupation_group__label AS occupation_group,
    description__text AS description_text,
    working_hours_type__label AS working_hours,
    duration__label AS duration_label,
    publication_date,
    application_deadline,
    occupation__label AS occupation_label,
    removed
FROM read_csv_auto('job_ads.csv', HEADER=TRUE)