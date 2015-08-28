import pandas as pd
import csv
import os
from os import walk
from sqlalchemy import create_engine
import config
import time
from datetime import datetime
from datetime import date
from dateutil.relativedelta import relativedelta


datadir = ""
dir = os.path.abspath(os.path.dirname("__file__"))
dir = dir + "\\data"

#################################################################################################
# Create one df object which contains all data from all states in all reports.
# Reports are formatted as follows:
# wbc_report_data_MONTH-YEAR.xlsx

f = []
for (dirpath, dirnames, filenames) in walk(dir):
    f.extend(filenames)
    break

reports = []
for filename in filenames:
    if 'wbc_report_data' in filename:
        print filename
        reports.append(filename)

states = ['arizona',
          'california',
          'colorado',
          'idaho',
          'montana',
          'nevada',
          'new mexico',
          'oregon',
          'texas',
          'utah',
          'washington',
          'wyoming']

df = pd.DataFrame()
for report in reports:
    for state in states:
        date = report[16:-5]
        report_file = dir + "\\" + report
        data = pd.read_excel(report_file, sheetname = state)
        data['date'] = date
        df = df.append(data)

df['States'] = df['States'].str.title()
df['Organization'] = df['Organization'].str.replace('Neil Helm', 'Neal Helm')

dates = pd.to_datetime(df['date'], format = "%m-%Y")
df['date'] = dates
most_recent = df['date'].max()

# #################################################################################################
# # Query in new data from panelists

engine = config.engine

new_report_all = df[df['date'] == most_recent]
new_date = most_recent + relativedelta(months =+ 1)
new_report_all['date'] = new_date

cols = new_report_all.columns.values.tolist()

new_data = pd.read_sql_table("load_table_new", engine)
del new_data['EmailAddress']
new_data = new_data[cols]

sub_dat = new_data['Organization'] + "-" + new_data['States']
new_report_all['sub_dat'] = new_report_all['Organization'] + "-" + new_report_all['States']

new_report_all = new_report_all[~new_report_all['sub_dat'].isin(sub_dat)]
del new_report_all['sub_dat']

new_report_all_v2 = new_report_all.append(new_data)
new_report_all_v2['States'] = new_report_all_v2['States'].str.lower()

states = new_report_all_v2['States'].unique()

most_recent_month = time.strftime("%m")
most_recent_month = most_recent_month.lstrip('0')
most_recent_year  = time.strftime("%Y")

most_recent = most_recent_month + "-" + most_recent_year

report_name = 'data/wbc_report_data-' + most_recent + ".xlsx"

writer = pd.ExcelWriter(report_name)

for state in states:
    temp_data = new_report_all_v2[new_report_all_v2['States'] == state]
    del temp_data['date']
    temp_data.to_excel(writer, state, index = False, )

writer.save()


