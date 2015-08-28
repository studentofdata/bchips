import requests
import os
import csv
import json
import pandas as pd
import pandas.io.sql as psql
import numpy as np
import subprocess
import time
import config
import qualtrics_clean


dir = os.path.abspath(os.path.dirname("__file__"))
datadir = dir + "\\data"

os.chdir(dir)

engine = config.engine


################################################################################################################
# Western Blue Chips
wbc_dep = psql.frame_query('Select * from wbc_deployment', engine)
wbc_dep['States'] = wbc_dep['States'].str.lower()

panelists = psql.frame_query('Select * from wbc_panelists', engine)

wbc_dep[['Q1A1','Q1A2','Q2A1','Q2A2','Q3A1','Q3A2','Q4A1','Q4A2','Q5A1','Q5A2',
          'Q2A1_ggr','Q2A2_ggr','Q2A1_mfg','Q2A2_mfg']] = wbc_dep[['Q1A1','Q1A2','Q2A1','Q2A2','Q3A1','Q3A2','Q4A1','Q4A2','Q5A1','Q5A2',
          'Q2A1_ggr','Q2A2_ggr','Q2A1_mfg','Q2A2_mfg']].convert_objects(convert_numeric = True)

wbc_dep_v2 = pd.pivot_table(wbc_dep, index = ['Organization'], columns = ['States'])

wbc_dep_v2 = wbc_dep_v2.reset_index()

wbc_dep_v2.columns = [''.join(col).strip() for col in wbc_dep_v2.columns.values]

wbc_dep_v3 = wbc_dep_v2.merge(panelists, on = 'Organization')

wbc_dep_v3_names = pd.Series(wbc_dep_v3.columns.values.tolist())
wbc_dep_v3.columns = wbc_dep_v3_names.replace(qualtrics_clean.import_panel_rename)

cols = list(wbc_dep_v3.columns.values)
cols.insert(0, cols.pop(cols.index('PrimaryEmail')))

wbc_dep_v3 = wbc_dep_v3.ix[:, cols]

wbc_dep_v3.to_csv("wbc_import_qualtrics_panel.csv", index = False)



#################################################################################################################


file = open('wbc_import_qualtrics_panel.csv','r').read()

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
                    'Name' : 'wbc - v2',
                    'ColumnHeaders' : 1,
                    'Email' : 1,
                    'Request' : 'importPanel',
                    'AllED' : 1}

# Download Data from the Qualtrics API
requests.post('https://survey.qualtrics.com/WRAPI/ControlPanel/api.php', params = qualtrics_params, data = file)


