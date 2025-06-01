{{ config(materialized='table') }}

SELECT *
FROM {{ ref('fct_job_ads') }}
WHERE occupation_group__label IN (
    'Företagssäljare',
    'Butikssäljare, fackhandel',
    'Butikssäljare, dagligvaror',
    'Eventsäljare och butiksdemonstratörer m.fl.',
    'Säljande butikschefer och avdelningschefer i butik',
    'Marknads- och försäljningsassistenter',
    'Inköps- och orderassistenter',
    'Inköpare och upphandlare',
    'Resesäljare och trafikassistenter m.fl.',
    'Marknadsanalytiker och marknadsförare m.fl.'
)
