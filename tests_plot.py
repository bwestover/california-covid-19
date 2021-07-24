import csv
import datetime
import sys
from matplotlib import pyplot as plt
from matplotlib.ticker import FuncFormatter

COUNTY = sys.argv[1]

with open('covid19cases_test.csv') as cases_csv:
    cases_csv_reader = csv.reader(cases_csv)
    # Data is from the California Health and Human Services portal - https://data.chhs.ca.gov/dataset/covid-19-time-series-metrics-by-county-and-state
    # Raw data headers
    #date,area,area_type,population,cases,cumulative_cases,deaths,cumulative_deaths,total_tests,cumulative_total_tests,positive_tests,cumulative_positive_tests,reported_cases,cumulative_reported_cases,reported_deaths,cumulative_reported_deaths,reported_tests


    # X Axis = Date converted to datetime
    # Bottom Bar = Positive tests
    # Top Bar = Total tests
    # Plot = Percent positive
    data = [
            [
                datetime.datetime.strptime(rows[0], "%Y-%m-%d"),
                int(float(rows[10] or 0)),
                int(float(rows[8] or 0)),
                int(float(rows[10] or 0)) / (int(float(rows[8])) or 1)
            ]
            for rows in cases_csv_reader
            if rows[0] and rows[8] and rows[10] and rows[1] == COUNTY
           ]

date = [row[0] for row in data]
positive_tests = [row[1] for row in data]
total_tests = [row[2] for row in data]
pct_positive = [row[3] for row in data]

fig, ax1 = plt.subplots()

ax1.set_xlabel('Date')
ax1.set_ylabel('Total / Positive Tests')
ax1.bar(date, positive_tests, color='tab:red')
ax1.bar(date, total_tests, color='tab:blue', bottom=positive_tests)
ax1.tick_params(axis='y')

ax2 = ax1.twinx()

ax2.set_ylabel('Percent Positive')
ax2.plot(date, pct_positive, color='#000000')
ax2.tick_params(axis='y')
ax2.yaxis.set_major_formatter(FuncFormatter(lambda y, _: '{:.0%}'.format(y)))

fig.tight_layout()
plt.title(f"Positive / Total tests for {COUNTY} county")
plt.show()
