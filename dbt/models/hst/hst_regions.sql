{{ config(
    materialized='view',
    schema='hst',
    alias='hst_regions'
) }}

SELECT DISTINCT
    region_id::INTEGER AS region_id,

    NULLIF(TRIM(country::TEXT), '')
        AS country,

    NULLIF(TRIM(city::TEXT), '')
        AS city

FROM {{ source('staging', 'regions') }}