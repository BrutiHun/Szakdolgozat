CREATE SCHEMA IF NOT EXISTS staging;

CREATE SCHEMA IF NOT EXISTS dwh;

CREATE TABLE staging.sales (
    sales_id        VARCHAR,
    sales_date      VARCHAR,
    store_id        VARCHAR,
    customer_id     VARCHAR,
    product_id      VARCHAR,
    promotion_id    VARCHAR,
    quantity        VARCHAR,
    unit_price      VARCHAR,
    total_price     VARCHAR,
    payment_type    VARCHAR
);

CREATE TABLE staging.stores (
    store_id        VARCHAR,
    store_name      VARCHAR,
    store_type      VARCHAR,
    region_id       VARCHAR
);

CREATE TABLE staging.loyalty_customers (
    customer_id     VARCHAR,
    first_name      VARCHAR,
    last_name       VARCHAR,
    gender          VARCHAR,
    birth_date      VARCHAR,
    region_id       VARCHAR
);

CREATE TABLE staging.products (
    product_id      VARCHAR,
    product_code    VARCHAR,
    category        VARCHAR,
    unit_price      VARCHAR,
    is_active       VARCHAR
);

CREATE TABLE staging.promotions (
    promotion_id    VARCHAR,
    product_id      VARCHAR,
    discount_percent VARCHAR,
    promotion_name  VARCHAR,
    start_date      VARCHAR,
    end_date        VARCHAR
);

CREATE TABLE staging.regions (
    region_id       VARCHAR,
    country         VARCHAR,
    city            VARCHAR
);

