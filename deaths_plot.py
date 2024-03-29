import csv
import datetime
import sys
from matplotlib import pyplot as plt

COUNTY = sys.argv[1]

with open('covid19cases_test.csv') as cases_csv:
    cases_csv_reader = csv.reader(cases_csv)
    # Data is from the California Health and Human Services portal - https://data.chhs.ca.gov/dataset/covid-19-time-series-metrics-by-county-and-state
    # Raw data headers
    #date,area,area_type,population,cases,cumulative_cases,deaths,cumulative_deaths,total_tests,cumulative_total_tests,positive_tests,cumulative_positive_tests,reported_cases,cumulative_reported_cases,reported_deaths,cumulative_reported_deaths,reported_tests

    # X Axis = Date converted to datetime
    # Y Axis = Total deaths
    data = [
            [
                datetime.datetime.strptime(rows[0], "%Y-%m-%d"),
                int(float(rows[6] or 0))
            ]
            for rows in cases_csv_reader
            if rows[0] and rows[1] == COUNTY
           ]

x = [row[0] for row in data]
y = [row[1] for row in data]

plt.title(f"Confirmed deaths for {COUNTY} county")
plt.bar(x, y)
plt.show()
