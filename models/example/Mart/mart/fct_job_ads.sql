{{ config(materialized='table') }}

SELECT
    a.id,
    a.publication_date,
    a.application_deadline,
    a.working_hours,
    o.occupation_label,
    o.occupation_group__label,
    e.employer__organization_number,
    aux.duration_label
FROM {{ ref('stg_job_ads') }} AS a
LEFT JOIN {{ ref('dim_occupation') }} AS o ON a.id = o.id
LEFT JOIN {{ ref('dim_employer') }} AS e ON a.employer__organization_number = e.employer__organization_number
LEFT JOIN {{ ref('dim_auxilliary_attributes') }} AS aux ON a.id = aux.id
WHERE a.id IS NOT NULL
