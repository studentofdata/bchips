import requests
import os
import csv
import json
import pandas as pd
import numpy as np
import subprocess
import time

#filepath = "C:\\Users\\rjrow.ASURITE\\bc\\import_qualtrics_panel.csv"
#basepath = "C:\\Users\\rjrow.ASURITE\\bc"
################################################################################################################
# Here we need to create the import_qualtrics_panel.csv, lucky for us it is technically the same exact thing as the
# deployment table used on the website (panelists most recent forecasts). Let's take this in, use it, and import it to the
# qualtrics system for use.






dir = os.path.abspath(os.path.dirname("__file__"))
dir = dir + "\\data"

os.chdir(basepath)

file = open('import_qualtrics_panel.csv','r').read()

## Now that we have our panel csv lets send it off to qualtrics

q_token = 'Eo9Cq2pIMlm9djm7obIjoIUNANYgxcG2fqM8QawD'
q_surveyID = 'SV_0PrXQuBvQeRAaxv'
q_libraryID = 'UR_1yKoy6MfnMpmHWZ'
q_user = 'wpcareyseid@asu.edu'

qualtrics_params = {   'User': q_user,
                    'Token' : q_token,
                    'Format' : 'JSON',
                    'Version' : '2.3',
                    'LibraryID' : q_libraryID,
                    'SurveyID' : q_surveyID,
                    'Name' : 'wbc_import',
                    'ColumnHeaders' : 1,
                    'Email' : 1,
                    'Request' : 'importPanel',
                    'AllED' : 1}

# Download Data from the Qualtrics API
requests.post('https://survey.qualtrics.com/WRAPI/ControlPanel/api.php', params = qualtrics_params, data = file)


