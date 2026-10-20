# Unemployment Analysis with Python

Task 2 of my CodeAlpha Data Science internship.

Analysis of the unemployment rate in Indian states, mainly to see what happened after Covid-19.

## How to run
The script uses `Unemployment in India.csv` (included in this folder). It covers 28 states from May 2019 to June 2020. The other file, `Unemployment_Rate_upto_11_2020.csv`, has data for Jan to Oct 2020 only and I did not use it.

    pip install -r requirements.txt
    python unemployment_analysis.py

Charts and tables are saved in the outputs folder.

## What the script does
- Cleans the data (strips spaces from column names, converts dates, drops the 28 blank rows at the end of the file)
- Plots the average unemployment rate over time with the lockdown date marked (25 March 2020)
- Compares the rate before and after the lockdown
- Finds which states have the highest average rate and which states increased the most
- Compares rural and urban areas
- Looks at month wise averages before Covid to check for seasonal patterns. The data is only about one year, so this is just a rough idea.
- Plots labour participation against unemployment rate

## Findings
- The average unemployment rate (average of all states) stayed around 9 to 10% from May 2019 to Feb 2020, went to 10.7% in March 2020, and jumped to 23.6% in April and 24.9% in May 2020 after the lockdown. In June it came back down to 11.9%.
- Employed people (sum of the Estimated Employed column) fell from about 391 million in March 2020 to 269 million in April, then recovered to 369 million by June.
- The average rate before Covid was about 9.6%, and during April to June 2020 it was about 20.2%. The maximum went up from 34.7% to 76.7%.
- Puducherry had the biggest increase (from about 1.6% to 57.7%), then Jharkhand, Tamil Nadu and Bihar. The highest single values were Puducherry 76.7%, Jharkhand 70.2% and Bihar 58.8%.
- Overall, Tripura, Haryana and Jharkhand had the highest average rates over the whole period.
- Urban areas were higher than rural both before Covid (10.9% vs 8.2%) and during Covid (22.1% vs 18.3%).
- Before Covid the monthly averages stay between about 8.9% and 10.7% with no clear pattern. There is only one year of data and April is missing, so I can't say anything solid about seasons.
- Labour participation rate and unemployment rate have almost no correlation (about 0.003).

The state averages are simple averages of the rows in the file, not weighted by population, so they are not the official national rate.

## Ideas for policy
- The jump in April and May shows how quickly jobs were lost in the lockdown, so support like cash transfers and rural employment schemes is needed fast in such a case.
- States that were hit the hardest (Puducherry, Jharkhand, Tamil Nadu, Bihar) need more targeted help.
- Urban unemployment was higher in both periods, so urban job schemes matter too, not only rural ones.
