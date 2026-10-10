
{{ config(
    materialized='view',
    schema='hst',
    alias='hst_stores'
) }}

SELECT DISTINCT
    store_id::INTEGER AS store_id,

    NULLIF(TRIM(store_name::TEXT), '')
        AS store_name,

    NULLIF(TRIM(store_type::TEXT), '')
        AS store_type,

    NULLIF(TRIM(region_id::TEXT), '')::INTEGER
        AS region_id

FROM {{ source('staging', 'stores') }}
