CREATE EXTERNAL TABLE moviesAndTv (
  `show_id` string, 
  `type` string, 
  `title` string, 
  `director` string, 
  `cast` string, 
  `country` string, 
  `date_added` string, 
  `release_year` bigint, 
  `rating` string, 
  `duration` string, 
  `listed_in` string, 
  `description` string)
STORED AS PARQUET
LOCATION 's3://doug-sql-athena-parquet/parquet_files'
TBLPROPERTIES ('parquet.compress'='SNAPPY');