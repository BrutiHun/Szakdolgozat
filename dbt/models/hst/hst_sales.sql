
{{ config(
    materialized='view',
    schema='hst',
    alias='hst_sales'
) }}

SELECT DISTINCT
    CASE
        WHEN TRIM(sales_id::TEXT) ~ '^\d+(\.0+)?$'
            THEN TRIM(sales_id::TEXT)::NUMERIC::INTEGER
        ELSE NULL
    END AS sales_id,

    CASE
        WHEN TRIM(sales_date::TEXT) ~ '^\d{4}-\d{2}-\d{2}$'
            THEN TO_DATE(TRIM(sales_date::TEXT), 'YYYY-MM-DD')
        WHEN TRIM(sales_date::TEXT) ~ '^\d{2}/\d{2}/\d{4}$'
            THEN TO_DATE(TRIM(sales_date::TEXT), 'DD/MM/YYYY')
        WHEN TRIM(sales_date::TEXT) ~ '^\d{2}-\d{2}-\d{4}$'
            THEN TO_DATE(TRIM(sales_date::TEXT), 'MM-DD-YYYY')
        WHEN TRIM(sales_date::TEXT) ~ '^[A-Za-z]+ \d{1,2}, \d{4}$'
            THEN TO_DATE(TRIM(sales_date::TEXT), 'FMMonth DD, YYYY')
        WHEN TRIM(sales_date::TEXT) ~ '^\d{1,2} [A-Za-z]+ \d{4}$'
            THEN TO_DATE(TRIM(sales_date::TEXT), 'DD FMMonth YYYY')
        ELSE NULL
    END AS sales_date,

    CASE
        WHEN TRIM(store_id::TEXT) ~ '^\d+(\.0+)?$'
            THEN TRIM(store_id::TEXT)::NUMERIC::INTEGER
        ELSE NULL
    END AS store_id,

    CASE
        WHEN TRIM(customer_id::TEXT) ~ '^\d+(\.0+)?$'
            THEN TRIM(customer_id::TEXT)::NUMERIC::INTEGER
        ELSE NULL
    END AS customer_id,

    CASE
        WHEN TRIM(product_id::TEXT) ~ '^\d+(\.0+)?$'
            THEN TRIM(product_id::TEXT)::NUMERIC::INTEGER
        ELSE NULL
    END AS product_id,

    CASE
        WHEN TRIM(promotion_id::TEXT) ~ '^\d+(\.0+)?$'
            THEN TRIM(promotion_id::TEXT)::NUMERIC::INTEGER
        ELSE NULL
    END AS promotion_id,

    CASE
        WHEN TRIM(quantity::TEXT) ~ '^-?\d+(\.0+)?$'
            THEN TRIM(quantity::TEXT)::NUMERIC::INTEGER
        ELSE NULL
    END AS quantity,

    CASE
        WHEN TRIM(unit_price::TEXT) ~ '^-?\d+(\.\d+)?$'
            THEN TRIM(unit_price::TEXT)::NUMERIC(12, 2)
        ELSE NULL
    END AS unit_price,

    CASE
        WHEN TRIM(total_price::TEXT) ~ '^-?\d+(\.\d+)?$'
            THEN TRIM(total_price::TEXT)::NUMERIC(12, 2)
        ELSE NULL
    END AS total_price,

    NULLIF(TRIM(payment_type::TEXT), '') AS payment_type

FROM {{ source('staging', 'sales') }}
