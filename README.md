# bchips
Blue Chips

Qualtrics is a survey tool we use for western blue chips


# Qualtrics Download
This file downloads data after a survey has been concluded


# Qualtrics Post Download
This file cleans and formats the data that has just been received. The new panelist's forecast submissions 
are then sent off to the database at the end of this file

# Qualtrics DB Import
This file is a utility for backing up the database with our .csv files. Every month a 'report' datasheet is created which represents
all of the panelists forecasts for that month. These .csv files should be used to create Western Blue Chip reports but here they are
used to create an Archive object which is sent off to the Archives in the database
