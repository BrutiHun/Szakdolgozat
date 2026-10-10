
{% snapshot stores_snapshot %}

{{
    config(
        target_schema='hst',
        unique_key='store_id',
        strategy='check',
        check_cols=[
            'store_name',
            'store_type',
            'region_id'
        ]
    )
}}

SELECT
    store_id,
    store_name,
    store_type,
    region_id
FROM {{ ref('hst_stores') }}

{% endsnapshot %}
