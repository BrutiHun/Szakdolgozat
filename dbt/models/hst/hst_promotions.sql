
{{ config(
    materialized='view',
    schema='hst',
    alias='hst_promotions'
) }}

SELECT DISTINCT
    promotion_id::INTEGER AS promotion_id,
    product_id::INTEGER AS product_id,

    NULLIF(TRIM(promotion_name::TEXT), '')
        AS promotion_name,

    NULLIF(TRIM(discount_percent::TEXT), '')::NUMERIC(7, 4)
        AS discount_percent,

    CASE
        WHEN TRIM(start_date::TEXT) ~ '^\d{4}-\d{2}-\d{2}$'
            THEN TO_DATE(TRIM(start_date::TEXT), 'YYYY-MM-DD')

        WHEN TRIM(start_date::TEXT) ~ '^\d{2}/\d{2}/\d{4}$'
            THEN TO_DATE(TRIM(start_date::TEXT), 'DD/MM/YYYY')

        WHEN TRIM(start_date::TEXT) ~ '^\d{2}-\d{2}-\d{4}$'
            THEN TO_DATE(TRIM(start_date::TEXT), 'MM-DD-YYYY')

        WHEN TRIM(start_date::TEXT) ~ '^[A-Za-z]+ \d{1,2}, \d{4}$'
            THEN TO_DATE(TRIM(start_date::TEXT), 'FMMonth DD, YYYY')

        WHEN TRIM(start_date::TEXT) ~ '^\d{1,2} [A-Za-z]+ \d{4}$'
            THEN TO_DATE(TRIM(start_date::TEXT), 'DD FMMonth YYYY')

        ELSE NULL
    END AS start_date,

    CASE
        WHEN TRIM(end_date::TEXT) ~ '^\d{4}-\d{2}-\d{2}$'
            THEN TO_DATE(TRIM(end_date::TEXT), 'YYYY-MM-DD')

        WHEN TRIM(end_date::TEXT) ~ '^\d{2}/\d{2}/\d{4}$'
            THEN TO_DATE(TRIM(end_date::TEXT), 'DD/MM/YYYY')

        WHEN TRIM(end_date::TEXT) ~ '^\d{2}-\d{2}-\d{4}$'
            THEN TO_DATE(TRIM(end_date::TEXT), 'MM-DD-YYYY')

        WHEN TRIM(end_date::TEXT) ~ '^[A-Za-z]+ \d{1,2}, \d{4}$'
            THEN TO_DATE(TRIM(end_date::TEXT), 'FMMonth DD, YYYY')

        WHEN TRIM(end_date::TEXT) ~ '^\d{1,2} [A-Za-z]+ \d{4}$'
            THEN TO_DATE(TRIM(end_date::TEXT), 'DD FMMonth YYYY')

        ELSE NULL
    END AS end_date

FROM {{ source('staging', 'promotions') }}
