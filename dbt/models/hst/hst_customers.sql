
{{ config(
    materialized='view',
    schema='hst',
    alias='hst_customers'
) }}

SELECT DISTINCT
    customer_id::INTEGER AS customer_id,

    NULLIF(TRIM(first_name::TEXT), '')
        AS first_name,

    NULLIF(TRIM(last_name::TEXT), '')
        AS last_name,

    NULLIF(TRIM(gender::TEXT), '')
        AS gender,

    CASE
        WHEN TRIM(birth_date::TEXT) ~ '^\d{4}-\d{2}-\d{2}$'
            THEN TO_DATE(TRIM(birth_date::TEXT), 'YYYY-MM-DD')

        WHEN TRIM(birth_date::TEXT) ~ '^\d{2}/\d{2}/\d{4}$'
            THEN TO_DATE(TRIM(birth_date::TEXT), 'DD/MM/YYYY')

        WHEN TRIM(birth_date::TEXT) ~ '^\d{2}-\d{2}-\d{4}$'
            THEN TO_DATE(TRIM(birth_date::TEXT), 'MM-DD-YYYY')

        WHEN TRIM(birth_date::TEXT) ~ '^[A-Za-z]+ \d{1,2}, \d{4}$'
            THEN TO_DATE(TRIM(birth_date::TEXT), 'FMMonth DD, YYYY')

        WHEN TRIM(birth_date::TEXT) ~ '^\d{1,2} [A-Za-z]+ \d{4}$'
            THEN TO_DATE(TRIM(birth_date::TEXT), 'DD FMMonth YYYY')

        ELSE NULL
    END AS birth_date,

    NULLIF(TRIM(region_id::TEXT), '')::INTEGER
        AS region_id

FROM {{ source('staging', 'loyalty_customers') }}
