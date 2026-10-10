
{% snapshot products_snapshot %}

{{
    config(
        target_schema='hst',
        unique_key='product_id',
        strategy='check',
        check_cols=[
            'product_code',
            'category',
            'unit_price',
            'is_active'
        ]
    )
}}

SELECT
    product_id,
    product_code,
    category,
    unit_price,
    is_active
FROM {{ ref('hst_products') }}

{% endsnapshot %}
