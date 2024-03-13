CREATE DATABASE zonal_statistics_db;


CREATE TABLE test_roi_tbl (
    image_date date,
    min double precision,
    max double precision,
    mean double precision,
    median double precision,
    std_dev double precision
)
