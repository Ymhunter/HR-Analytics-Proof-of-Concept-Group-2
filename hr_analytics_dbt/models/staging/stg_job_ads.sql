-- models/staging/stg_job_ads.sql

SELECT
    id AS job_id,
    label,
    relevance,
    webpage_url,
    salary_description,
    application_deadline,
    occupation_id,
    occupation_name,
    occupation_field__label AS occupation_field,
    employer__name AS employer_name,
    workplace_address__city AS workplace_city
FROM raw_job_ads.job_ads_rp_tn_bx_g_ex_z

UNION ALL

SELECT
    id AS job_id,
    label,
    relevance,
    webpage_url,
    salary_description,
    application_deadline,
    occupation_id,
    occupation_name,
    occupation_field__label AS occupation_field,
    employer__name AS employer_name,
    workplace_address__city AS workplace_city
FROM raw_job_ads.job_ads_nyw6_m_p6_vwf

UNION ALL

SELECT
    id AS job_id,
    label,
    relevance,
    webpage_url,
    salary_description,
    application_deadline,
    occupation_id,
    occupation_name,
    occupation_field__label AS occupation_field,
    employer__name AS employer_name,
    workplace_address__city AS workplace_city
FROM raw_job_ads.job_ads_sc_ky_fhb_7w_t
