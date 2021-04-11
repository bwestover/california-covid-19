import csv
import datetime
import sys
from matplotlib import pyplot as plt

COUNTY = sys.argv[1]

with open('covid19cases_test.csv') as cases_csv:
    cases_csv_reader = csv.reader(cases_csv)
    # Data is from the California Health and Human Services portal - https://data.chhs.ca.gov/dataset/covid-19-time-series-metrics-by-county-and-state
    # Raw data headers
    # DATE,AREA,AREA_TYPE,POPULATION,CASES,DEATHS,TOTAL_TESTS,POSITIVE_TESTS,REPORTED_CASES,REPORTED_DEATHS,REPORTED_TESTS

    # X Axis = Date converted to datetime
    # Y Axis = Death count per 100K (deaths / population * 100,000)
    data = [
            [
                datetime.datetime.strptime(rows[0], "%Y-%m-%d"),
                (int(float(rows[5] or 0)) / int(float(rows[3] or 0)))*100000
            ]
            for rows in cases_csv_reader
            if rows[0] and rows[1] == COUNTY
           ]

x = [row[0] for row in data]
y = [row[1] for row in data]
#DEBUG
#print(x)
#print(y)

plt.title(f"Confirmed deaths per 100K for {COUNTY} county")
plt.bar(x, y)
plt.show()