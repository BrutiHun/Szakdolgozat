
{% snapshot promotions_snapshot %}

{{
    config(
        target_schema='hst',
        unique_key='promotion_id',
        strategy='check',
        check_cols=[
            'product_id',
            'promotion_name',
            'discount_percent',
            'start_date',
            'end_date'
        ]
    )
}}

SELECT
    promotion_id,
    product_id,
    promotion_name,
    discount_percent,
    start_date,
    end_date
FROM {{ ref('hst_promotions') }}

{% endsnapshot %}
