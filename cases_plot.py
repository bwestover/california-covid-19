import csv
import datetime
import sys
from matplotlib import pyplot as plt

COUNTY = sys.argv[1]

with open('2019_ca_population_est.csv') as population_csv:
    pop_csv_reader = csv.reader(population_csv)
    # Data is 2019 estimate from U.S. census bureau - https://www2.census.gov/programs-surveys/popest/tables/2010-2019/counties/totals/co-est2019-annres-06.xlsx
    county_population = {rows[0]:rows[1] for rows in pop_csv_reader}

pop = int(county_population[COUNTY])

#DEBUG
#print(f"{COUNTY} population: {pop}")

with open('statewide_cases.csv') as cases_csv:
    cases_csv_reader = csv.reader(cases_csv)
    # Data is from the California Open Data portal - https://data.ca.gov/dataset/covid-19-cases
    # Raw data headers
    # county,totalcountconfirmed,totalcountdeaths,newcountconfirmed,newcountdeaths,date
    
    # X Axis = Date converted to datetime
    # Y Axis = Case count per 100K (newcountconfirmed / county population * 100,000)
    data = [
            [
                datetime.datetime.strptime(rows[5], "%Y-%m-%d"), 
                (int(rows[3])/pop)*100000
            ] 
            for rows in cases_csv_reader 
            if rows[0] == COUNTY
            ]

x = [row[0] for row in data]
y = [row[1] for row in data]
#DEBUG
#print(x)
#print(y)

plt.title(f"Confirmed cases per 100K for {COUNTY} county")
plt.bar(x, y)
plt.show()
