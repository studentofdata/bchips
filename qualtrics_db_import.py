import pandas as pd
import csv
import os
from os import walk
from sqlalchemy import create_engine
import config

datadir = ""
dir = os.path.abspath(os.path.dirname("__file__"))
dir = dir + "\\data"

engine = config.engine

f = []
for (dirpath, dirnames, filenames) in walk(dir):
    f.extend(filenames)
    break

reports = []
for filename in filenames:
    if 'wbc_report' in filename:
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
        data = pd.read_excel(report_file, sheetname = "arizona")
        data['date'] = date
        df = df.append(data)

dates = pd.to_datetime(df['date'], format = "%m-%Y")
df['date'] = dates
df = df.rename(columns={'States':'State'})

df.to_sql('wbc_archive_load_test', engine, flavor = 'mysql', if_exists = 'replace', index = False)


