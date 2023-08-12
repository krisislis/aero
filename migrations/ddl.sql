CREATE SCHEMA staging;

CREATE TABLE staging.cannabis
(
    id                       bigint,
    uid                      text,
    strain                   text,
    cannabinoid_abbreviation text,
    cannabinoid              text,
    terpene                  text,
    medical_use              text,
    health_benefit           text,
    category                 text,
    type                     text,
    buzzword                 text,
    brand                    text,
    _created_at              timestamptz DEFAULT now()
);
