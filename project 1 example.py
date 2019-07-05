import pandas as pd
import numpy as np
import csv
from datetime import datetime
from datetime import date
import calendar

# plot modules
import matplotlib.pyplot as plt
import matplotlib
%matplotlib inline
matplotlib.style.use("ggplot")

path = "http://web.mta.info/developers/data/nyct/turnstile/turnstile_190629.txt"
new_cols = ["C/A", "UNIT", "SCP", "STATION", "LINENAME", "DIVISION", "DATE", "TIME", "DESC", "ENTRIES", "EXITS"]
data = pd.read_csv(path, sep=",", header=0, names=new_cols)
data["TIME"]
# drop NaNs
data = data.dropna()

# convert date and time types to datetime
data["TIME"] = (pd.to_datetime(data["TIME"])).dt.time
data["DAY_OF_WEEK"] = (pd.to_datetime(data["DATE"])).dt.weekday_name.str.strip() # by day of the week
data["MONTH"] = (pd.to_datetime(data["DATE"])).dt.month.str.strip() # by month
data['MONTH'] = data['MONTH'].apply(lambda x: calendar.month_abbr[x])

# make turnstile passes column
data["TURNSTILE_PASSES"] = data["ENTRIES"] + data["EXITS"]

### Traffic by stations and turnstile passes
##### filter by stations from end of each day
station_datetime = ["STATION", "MONTH", "DATE", "DAY_OF_WEEK", "TIME"]
data_by_station_datetime = (data.set_index(station_datetime).sort_index())
s = data_by_station_datetime.loc[data_by_station_datetime.TURNSTILE_PASSES > 1000000000, ]
t = data_by_station_datetime.loc[(data_by_station_datetime.EXITS > data_by_station_datetime.ENTRIES) & (data_by_station_datetime.TURNSTILE_PASSES > 1000000000)]
t.head()
##### filter by maximum turnstile passes per time interval


##### stations and turnstile passes table
total_station_activity = data[["STATION", "TURNSTILE_PASSES"]].copy()
total_station_activity

### Traffic by week day and turnstile passes
weekday_station_activity = data[["DAY_OF_WEEK", "TURNSTILE_PASSES"]].copy()
weekday_station_activity

### Traffic by month and turnstile passes
monthly_station_activity = data[["MONTH", "TURNSTILE_PASSES"]].copy()
monthly_station_activity = monthly_station_activity.set_index("MONTH").sort_index()
monthly_station_activity.tail(50)

### Traffic by hour and entries

### Traffic by hour and exits
