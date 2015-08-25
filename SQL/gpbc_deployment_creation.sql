DROP TABLE gpbc_deployment;

# Q1:: Population
# Q2:: Personal Income
# Q3:: Retail Sales
# Q4:: Wage & Salary Employment
# Q5:: Manufacturing Employment
# Q6:: Constuction Employment

CREATE TABLE `gpbc_deployment` (
  `year` bigint(20) DEFAULT NULL,
  `organization` text,
  `Q1` double DEFAULT NULL,
  `Q2` double DEFAULT NULL,
  `Q3` double DEFAULT NULL,
  `Q4` double DEFAULT NULL,
  `Q5` double DEFAULT NULL,
  `Q6` double DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOAD DATA LOCAL INFILE 'C:/Users/rjrow.ASURITE/Desktop/wbc_gpbc/live_data_store/gpbc_2ndQtr_2015.csv' INTO TABLE gpbc_deployment
COLUMNS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(year, organization, Q1, Q2, Q3, Q4, Q5, Q6);
