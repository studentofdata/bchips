DROP TABLE IF EXISTS gpbc_industrial;

# Q1:: Construction
# Q2:: Vacancy (Year End%)
# Q3:: Absorpotion

CREATE TABLE `gpbc_industrial` (
  `year` bigint(20) DEFAULT NULL,
  `organization` text,
  `Q1` text DEFAULT NULL,
  `Q2` text DEFAULT NULL,
  `Q3` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOAD DATA LOCAL INFILE 'C:/Users/rjrow.ASURITE/Desktop/wbc_gpbc/live_data_store/gpbc_industrial.csv' INTO TABLE gpbc_industrial
COLUMNS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(year, organization, Q1, Q2, Q3);
