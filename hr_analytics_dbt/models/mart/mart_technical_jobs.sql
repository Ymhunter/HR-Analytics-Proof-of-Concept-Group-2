WITH fct AS (
    SELECT * FROM {{ ref('fct_job_ads') }}
),
job_details AS (
    SELECT * FROM {{ ref('dim_job_details') }}
),
occupation AS (
    SELECT * FROM {{ ref('dim_occupation') }}
),
employer AS (
    SELECT * FROM {{ ref('dim_employer') }}
),
auxiliary AS (
    SELECT * FROM {{ ref('dim_auxiliary_attributes') }}
)

SELECT
    f.job_details_id,
    jd.headline,
    jd.description,
    jd.salary_type,
    jd.duration,
    jd.scope_of_work__min,
    jd.scope_of_work__max,

    f.occupation_id,
    o.occupation,
    o.occupation_group,
    o.occupation_field,

    f.employer_id,
    e.employer_name,
    e.employer__workplace,
    e.employer__organization_number,
    e.workplace_street_address,
    e.workplace_address__region,
    e.workplace_address__postcode,
    e.workplace_address__city,
    e.workplace_address__country,

    f.auxiliary_attributes_id,
    a.experience_required,
    a.driver_license,
    a.access_to_own_car,

    f.vacancies,
    f.relevance,
    f.application_deadline

FROM fct f
JOIN job_details jd ON f.job_details_id = jd.job_details_id
JOIN occupation o ON f.occupation_id = o.occupation_id
JOIN employer e ON f.employer_id = e.employer_id
JOIN auxiliary a ON f.auxiliary_attributes_id = a.auxiliary_attributes_id
