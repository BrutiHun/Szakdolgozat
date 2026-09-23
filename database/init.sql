CREATE SCHEMA IF NOT EXISTS staging;

CREATE SCHEMA IF NOT EXISTS dwh;

CREATE SCHEMA IF NOT EXISTS control;

CREATE TABLE control.etl_runs (
    run_id          BIGSERIAL PRIMARY KEY,
    pipeline_name   VARCHAR(100) NOT NULL,
    start_time      TIMESTAMP NOT NULL,
    end_time        TIMESTAMP,
    status          VARCHAR(20) NOT NULL,
    source_rows     INTEGER,
    processed_rows  INTEGER,
    failed_rows     INTEGER,
    error_message   TEXT
);

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





CREATE TABLE dwh.dim_dates (
    date_key        INTEGER PRIMARY KEY,
    date            DATE NOT NULL,
    year            INTEGER NOT NULL,
    quarter         INTEGER NOT NULL,
    month           INTEGER NOT NULL,
    day             INTEGER NOT NULL,
    week            INTEGER NOT NULL,
    is_weekend      BOOLEAN NOT NULL
);

CREATE TABLE dwh.dim_stores (
    store_key       INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    store_id        INTEGER NOT NULL,
    store_name      VARCHAR(100),
    store_type      VARCHAR(50),
    city            VARCHAR(100),
    country         VARCHAR(100),
    valid_from      DATE NOT NULL,
    valid_to        DATE
);

CREATE TABLE dwh.dim_customers (
    customer_key    INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    customer_id     INTEGER NOT NULL,
    gender          VARCHAR(25),
    age_group       VARCHAR(50),
    birth_year      INTEGER,
    city            VARCHAR(100),
    valid_from      DATE NOT NULL,
    valid_to        DATE
);

CREATE TABLE dwh.dim_products (
    product_key     INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    product_id      INTEGER NOT NULL,
    product_code    VARCHAR(50),
    category        VARCHAR(100),
    unit_price      NUMERIC(12, 2),
    is_active       BOOLEAN,
    valid_from      DATE NOT NULL,
    valid_to        DATE
);

CREATE TABLE dwh.dim_promotions (
    promotion_key   INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    promotion_id    INTEGER NOT NULL,
    product_id      INTEGER,
    discount_percent INTEGER,
    promotion_name  VARCHAR(100),
    start_date      DATE,
    end_date        DATE
);

CREATE TABLE dwh.fact_sales (
    sales_key       BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    date_key        INTEGER NOT NULL,
    store_key       INTEGER NOT NULL,
    customer_key    INTEGER,
    product_key     INTEGER NOT NULL,
    promotion_key   INTEGER,
    quantity        INTEGER,
    unit_price      NUMERIC(12, 2),
    total_price     NUMERIC(12, 2),
    discount        NUMERIC(5, 2),

    CONSTRAINT fk_fact_date
        FOREIGN KEY (date_key)
        REFERENCES dwh.dim_dates(date_key),

    CONSTRAINT fk_fact_store
        FOREIGN KEY (store_key)
        REFERENCES dwh.dim_stores(store_key),

    CONSTRAINT fk_fact_customer
        FOREIGN KEY (customer_key)
        REFERENCES dwh.dim_customers(customer_key),

    CONSTRAINT fk_fact_product
        FOREIGN KEY (product_key)
        REFERENCES dwh.dim_products(product_key),

    CONSTRAINT fk_fact_promotion
        FOREIGN KEY (promotion_key)
        REFERENCES dwh.dim_promotions(promotion_key)
);