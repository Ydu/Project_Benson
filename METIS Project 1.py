ADD TITLE # common modules


import os
import re
import pandas as pd
import numpy as np
from datetime import datetime
from datetime import date
import calendar

# plot modules
import matplotlib.pyplot as plt
import matplotlib
%matplotlib inline
matplotlib.style.use("ggplot")

### 2018 DATASETS FROM BEGINNING OF MONTH
new_cols = ["C/A", "UNIT", "SCP", "STATION", "LINENAME", "DIVISION", "DATE", "TIME", "DESC", "ENTRIES", "EXITS"]

jan06_2018_path = "http://web.mta.info/developers/data/nyct/turnstile/turnstile_180106.txt"
jan06_2018_mta_data = pd.read_csv(jan06_2018_path, sep=",", header=0, names=new_cols)

feb03_2018_path = "http://web.mta.info/developers/data/nyct/turnstile/turnstile_180203.txt"
feb03_2018_mta_data = pd.read_csv(feb03_2018_path, sep=",", header=0, names=new_cols)

mar03_2018_path = "http://web.mta.info/developers/data/nyct/turnstile/turnstile_180303.txt"
mar03_2018_mta_data = pd.read_csv(mar03_2018_path, sep=",", header=0, names=new_cols)

apr07_2018_path = "http://web.mta.info/developers/data/nyct/turnstile/turnstile_180407.txt"
apr07_2018_mta_data = pd.read_csv(apr07_2018_path, sep=",", header=0, names=new_cols)

may05_2018_path = "http://web.mta.info/developers/data/nyct/turnstile/turnstile_180505.txt"
may05_2018_mta_data = pd.read_csv(may05_2018_path, sep=",", header=0, names=new_cols)

jun02_2018_path = "http://web.mta.info/developers/data/nyct/turnstile/turnstile_180602.txt"
jun02_2018_mta_data = pd.read_csv(jun02_2018_path, sep=",", header=0, names=new_cols)

jul07_2018_path = "http://web.mta.info/developers/data/nyct/turnstile/turnstile_180707.txt"
jul07_2018_mta_data = pd.read_csv(jul07_2018_path, sep=",", header=0, names=new_cols)

aug04_2018_path = "http://web.mta.info/developers/data/nyct/turnstile/turnstile_180804.txt"
aug04_2018_mta_data = pd.read_csv(aug04_2018_path, sep=",", header=0, names=new_cols)

sep01_2018_path = "http://web.mta.info/developers/data/nyct/turnstile/turnstile_180901.txt"
sep01_2018_mta_data = pd.read_csv(sep01_2018_path, sep=",", header=0, names=new_cols)

oct06_2018_path = "http://web.mta.info/developers/data/nyct/turnstile/turnstile_181006.txt"
oct06_2018_mta_data = pd.read_csv(oct06_2018_path, sep=",", header=0, names=new_cols)

nov03_2018_path = "http://web.mta.info/developers/data/nyct/turnstile/turnstile_181103.txt"
nov03_2018_mta_data = pd.read_csv(nov03_2018_path, sep=",", header=0, names=new_cols)

dec01_2018_path = "http://web.mta.info/developers/data/nyct/turnstile/turnstile_181103.txt"
dec01_2018_mta_data = pd.read_csv(dec01_2018_path, sep=",", header=0, names=new_cols)

mta_datasets_2018 = [jan06_2018_mta_data, feb03_2018_mta_data, mar03_2018_mta_data,
apr07_2018_path, may05_2018_mta_data, jun02_2018_mta_data, jul07_2018_mta_data, aug04_2018_mta_data,
sep01_2018_mta_data, oct06_2018_mta_data, nov03_2018_mta_data, dec01_2018_mta_data]

####### SAMPLE DATASET
### looking at the most recent MTA data from June 29, 2019 in NY
path = "http://web.mta.info/developers/data/nyct/turnstile/turnstile_190629.txt"
new_cols = ["C/A", "UNIT", "SCP", "STATION", "LINENAME", "DIVISION", "DATE", "TIME", "DESC", "ENTRIES", "EXITS"]
MTA_data = pd.read_csv(path, sep=",", header=0, names=new_cols)

### add turnstile passes column
MTA_data['TURNSTILE_PASSES'] = MTA_data['ENTRIES'] + MTA_data['EXITS']
MTA_data.sample(10)

## add day of the week column
MTA_data["DATE"] = pd.to_datetime(MTA_data["DATE"])
days = [calendar.day_name[date.weekday()] for date in MTA_data["DATE"]]
MTA_data["DAY_OF_WEEK"] = days

### sort and group by date
MTA_data["DATE"] = MTA_data["DATE"]
date_grouped_MTA_data = MTA_data.groupby("DATE").count()
date_sorted_MTA_data = MTA_data.sort_values("DATE")
# rearrange columns
cols = MTA_data.columns.tolist()
len(cols)
c1, c2, c3 = list(cols[:7]), cols[-1:], list(cols[7:-1])
cols = c1 + c2 + c3
cols
MTA_data = MTA_data[cols]

# new DataFrame with relevant data
condensed_cols = [cols[3], cols[6], cols[7], cols[8], cols[10], cols[11], cols[-1]]
condensed_MTA_data = MTA_data[condensed_cols]
condensed_MTA_datas

### 378 different subway stations
len(MTA_data.STATION.unique())

### group by columns and sort by highest activity
grouped_by_station = condensed_MTA_data.groupby('STATION').count().sort_values("DATE", ascending=False)
grouped_by_station
grouped_by_time = condensed_MTA_data.groupby('TIME').count()
grouped_by_time.sample(10)
