DROP TABLE IF EXISTS gpbc_residential;

# Q1:: Single-family Permits
# Q2:: Multi-family Permits
# Q3:: Apartment Vacancy (Q4 %)
# Q4:: Apartment Absorption

CREATE TABLE `gpbc_residential` (
  `year` bigint(20) DEFAULT NULL,
  `organization` text,
  `Q1` text DEFAULT NULL,
  `Q2` text DEFAULT NULL,
  `Q3` text DEFAULT NULL,
  `Q4` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOAD DATA LOCAL INFILE 'C:/Users/rjrow.ASURITE/Desktop/wbc_gpbc/live_data_store/gpbc_residential.csv' INTO TABLE gpbc_residential
COLUMNS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(year, organization, Q1, Q2, Q3, Q4);

