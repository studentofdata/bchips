#DROP TABLE wbc_panelists;

# FirstName
# LastName
# Email
# Organization
# arizona
# california
# colorado
# idaho
# montana
# nevada
# new.mexico
# oregon
# texas
# utah
# washington
# wyoming


CREATE TABLE `wbc_panelists` (
  `FirstName` varchar(50) DEFAULT NULL,
  `LastName` varchar(50) DEFAULT NULL,
  `Email` varchar(50) DEFAULT NULL,
  `Organization` varchar(95) DEFAULT NULL,
  `arizona` int DEFAULT NULL,
  `california` int DEFAULT NULL,
  `colorado` int DEFAULT NULL,
  `idaho` int DEFAULT NULL,
  `montana` int DEFAULT 0,
  `nevada` int DEFAULT 0,
  `new.mexico` int DEFAULT 0,
  `oregon` int DEFAULT 0,
  `texas` int DEFAULT 0,
  `utah` int DEFAULT 0,
  `washington` int DEFAULT 0,
  `wyoming` int DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOAD DATA LOCAL INFILE 'C:/Users/rjrow.ASURITE/Desktop/wbc_gpbc/data/panelists_official.csv' INTO TABLE wbc_panelists
COLUMNS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(FirstName,
LastName,
Email,
Organization,
arizona,
california,
colorado,
idaho,
montana,
nevada,
new.mexico,
oregon,
texas,
utah,
washington,
wyoming);
