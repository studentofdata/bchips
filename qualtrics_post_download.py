import os
import time
import datetime
import pandas as pd
import qualtrics_clean
import config
from sqlalchemy import create_engine

##
dir = os.path.abspath(os.path.dirname(__file__))
datadir = dir + "\\data"
os.chdir(datadir)

now = datetime.datetime.now()

engine = config.engine

##
wbc = pd.read_csv("qualtrics_pull_wbc_03_08_2015.csv")
names = wbc.iloc[0,].tolist()
wbc.columns = names
wbc = wbc.iloc[1:,]

wbc = wbc.drop(['Name','Finished','ResponseID','ResponseSet','ExternalDataReference','IPAddress','Status','StartDate','EndDate'], axis=1)
wbc = wbc.drop(qualtrics_clean.exclude_columns, axis=1)

wbc_melted = pd.melt(wbc, ["EmailAddress", "Organization"])
wbc_v2 = wbc_melted.dropna(subset = ['value'])
wbc_v2 = wbc_v2[~wbc_v2['variable'].str.contains('comment')]

split_columns = pd.DataFrame(wbc_v2['variable'].str.split('-',2).tolist(), columns = ['State','Year','Qs'])
wbc_v2 = wbc_v2.reset_index()
del wbc_v2['index']
wbc_v2['State'] = split_columns['State']
wbc_v2['Year'] = split_columns['Year']
wbc_v2['Qs'] = split_columns['Qs']

wbc_v3 = pd.DataFrame(wbc_v2)
wbc_v3['value'] = wbc_v3['value'].astype(float)

## Amend this section of code when comments become relevant, for now they are discarded

wbc_v3 = pd.pivot_table(wbc_v3, values = 'value', index = ['EmailAddress','Organization','State','Year'],
               columns = ['Qs'])

wbc_v3 = wbc_v3.reset_index()

years = wbc_v3['Year'].unique().tolist()
years.sort()

answers = ['A1','A2']
answers_mapping = dict(zip(years,answers))
wbc_v3['As'] = wbc_v3['Year'].map(answers_mapping)

wbc_v3_names = pd.Series(wbc_v3.columns.values.tolist())
wbc_v3.columns = wbc_v3_names.replace(qualtrics_clean.column_rename)

wbc_v4 = pd.pivot_table(wbc_v3, index=['EmailAddress','Organization','State'],
                          columns = ['As'])

wbc_v4.columns = [''.join(col).strip() for col in wbc_v4.columns.values]

wbc_v4 = wbc_v4.reset_index()

wbc_v4_names = pd.Series(wbc_v4.columns.values.tolist())
wbc_v4.columns = wbc_v4_names.replace(qualtrics_clean.final_column_rename)

for name in qualtrics_clean.master_column_names:
    if name not in wbc_v4:
        wbc_v4[name] = ""

date = time.strftime("%d_%m_%Y")
file_name = "wbc_download_" + date + ".csv"

date_wbc = str(now.month) + "-" + str(now.year)
dates = pd.to_datetime(date_wbc, format = "%m-%Y")

wbc_v4['date'] = dates


wbc_v4.to_sql('load_table_new', engine, flavor = 'mysql', if_exists = 'replace', index = False)
wbc_v4.to_csv(file_name)

