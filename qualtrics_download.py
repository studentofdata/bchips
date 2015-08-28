import requests
import os
import csv
import json
import subprocess
import time


dir = os.path.abspath(os.path.dirname(__file__))
datadir = dir + "\\data"
os.chdir(datadir)


most_recent = time.strftime("%d_%m_%Y")

qualtrics_params = {'Request' : 'getLegacyResponseData',
					'User': 'wpcareyseid@asu.edu',
					'Token' : 'Eo9Cq2pIMlm9djm7obIjoIUNANYgxcG2fqM8QawD',
					'SurveyID' : 'SV_0PrXQuBvQeRAaxv',
					'Format' : 'CSV',
                    'Labels' : '1',
					'Version' : '2.3'}

# Download Data from the Qualtrics API
r = requests.get('https://survey.qualtrics.com/WRAPI/ControlPanel/api.php', params = qualtrics_params)

pull_name = "qualtrics_pull_wbc_" + most_recent + ".csv"

file = open(pull_name,'w+')

with file as outfile:
    outfile.write(r.text.encode('utf-8'))




qualtrics_params = {'Request' : 'getLegacyResponseData',
					'User': 'wpcareyseid@asu.edu',
					'Token' : 'Eo9Cq2pIMlm9djm7obIjoIUNANYgxcG2fqM8QawD',
					'SurveyID' : 'SV_0GSrDtYvoS62wvz',
					'Format' : 'CSV',
                    'Labels' : '1',
					'Version' : '2.3'}

# Download Data from the Qualtrics API
r = requests.get('https://survey.qualtrics.com/WRAPI/ControlPanel/api.php', params = qualtrics_params)

gpbc_pull_name = "qualtrics_pull_gpbc_" + most_recent + ".csv"

file = open(gpbc_pull_name, 'w+')

with file as outfile:
    outfile.write(r.text.encode('utf-8'))

os.chdir(dir)