-- models/staging/stg_job_ads.sql

SELECT
    id AS job_id,
    external_id AS employer_id,
    label,
    relevance,
    webpage_url,
    headline,
    description__text_formatted AS description_text_formatted,
    salary_description,
    application_deadline,
    occupation_id,
    occupation_name,
    occupation_field__label AS occupation_field,
    employer__organization_number AS employer_organization_number,
    employer__name AS employer_name,
    workplace_address__city AS workplace_city,
    workplace_address__street_address AS workplace_street_address,
    workplace_address__region AS workplace_region,
    workplace_address__postcode AS workplace_postcode,
    workplace_address__country_code AS workplace_country,
    employment_type__label AS employment_type
FROM raw_job_ads.job_ads_rp_tn_bx_g_ex_z

UNION ALL

SELECT
    id AS job_id,
    external_id AS employer_id,
    label,
    relevance,
    webpage_url,
    headline,
    description__text_formatted AS description_text_formatted,
    salary_description,
    application_deadline,
    occupation_id,
    occupation_name,
    occupation_field__label AS occupation_field,
    employer__organization_number AS employer_organization_number,
    employer__name AS employer_name,
    workplace_address__city AS workplace_city,
    workplace_address__street_address AS workplace_street_address,
    workplace_address__region AS workplace_region,
    workplace_address__postcode AS workplace_postcode,
    workplace_address__country_code AS workplace_country,
    employment_type__label AS employment_type
FROM raw_job_ads.job_ads_nyw6_m_p6_vwf

UNION ALL

SELECT
    id AS job_id,
    external_id AS employer_id,
    label,
    relevance,
    webpage_url,
    headline,
    description__text_formatted AS description_text_formatted,
    salary_description,
    application_deadline,
    occupation_id,
    occupation_name,
    occupation_field__label AS occupation_field,
    employer__organization_number AS employer_organization_number,
    employer__name AS employer_name,
    workplace_address__city AS workplace_city,
    workplace_address__street_address AS workplace_street_address,
    workplace_address__region AS workplace_region,
    workplace_address__postcode AS workplace_postcode,
    workplace_address__country_code AS workplace_country,
    employment_type__label AS employment_type
FROM raw_job_ads.job_ads_sc_ky_fhb_7w_t
