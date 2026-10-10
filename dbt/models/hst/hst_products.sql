
{{ config(
    materialized='view',
    schema='hst',
    alias='hst_products'
) }}

SELECT DISTINCT
    product_id::INTEGER AS product_id,
    NULLIF(TRIM(product_code::TEXT), '')::VARCHAR(50)
        AS product_code,
    NULLIF(TRIM(category::TEXT), '')::VARCHAR(100)
        AS category,
    NULLIF(TRIM(unit_price::TEXT), '')::NUMERIC(12, 2)
        AS unit_price,
    CASE
        WHEN LOWER(TRIM(is_active::TEXT))
            IN ('true', 't', '1', 'igen', 'yes')
            THEN TRUE
        WHEN LOWER(TRIM(is_active::TEXT))
            IN ('false', 'f', '0', 'nem', 'no')
            THEN FALSE
        ELSE NULL
    END AS is_active
FROM {{ source('staging', 'products') }}
