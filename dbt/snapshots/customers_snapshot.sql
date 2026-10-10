
{% snapshot customers_snapshot %}

{{
    config(
        target_schema='hst',
        unique_key='customer_id',
        strategy='check',
        check_cols=[
            'first_name',
            'last_name',
            'gender',
            'birth_date',
            'region_id'
        ]
    )
}}

SELECT
    customer_id,
    first_name,
    last_name,
    gender,
    birth_date,
    region_id
FROM {{ ref('hst_customers') }}

{% endsnapshot %}
