import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# data is from May 2019 to June 2020
df = pd.read_csv("Unemployment in India.csv", encoding="utf-8-sig")
df.columns = df.columns.str.strip()
df = df.rename(columns={
    "Estimated Unemployment Rate (%)": "rate",
    "Estimated Employed": "employed",
    "Estimated Labour Participation Rate (%)": "participation",
})

os.makedirs("outputs", exist_ok=True)

print(df.shape)
print(df.isnull().sum())

# the file has some completely empty rows at the end of the table, removing them
df = df.dropna()
print("after removing empty rows:", df.shape)
print("duplicates:", df.duplicated().sum())

df["Region"] = df["Region"].str.strip()
df["Area"] = df["Area"].str.strip()
df["Date"] = pd.to_datetime(df["Date"].str.strip(), dayfirst=True)
print("regions:", df["Region"].nunique())
print(df["Date"].min().date(), "to", df["Date"].max().date())

# lockdown started on 25 march 2020, so april onwards is covid period
lockdown = pd.Timestamp("2020-03-25")
df["period"] = "before covid"
df.loc[df["Date"] >= "2020-04-01", "period"] = "covid"
df["month"] = df["Date"].dt.month

# overall trend
monthly = df.groupby("Date")["rate"].mean()
plt.figure(figsize=(10, 5))
plt.plot(monthly.index, monthly.values, marker="o")
plt.axvline(lockdown, color="red", linestyle="--", label="lockdown")
plt.title("Average unemployment rate per month")
plt.ylabel("unemployment rate (%)")
plt.legend()
plt.savefig("outputs/trend.png")
plt.close()

# before vs during covid
print(df.groupby("period")["rate"].describe())
sns.boxplot(data=df, x="period", y="rate", order=["before covid", "covid"])
plt.title("Unemployment rate before and during covid")
plt.savefig("outputs/covid_boxplot.png")
plt.close()

# by state
by_region = df.groupby("Region")["rate"].mean().sort_values(ascending=False)
print(by_region)
plt.figure(figsize=(8, 9))
sns.barplot(x=by_region.values, y=by_region.index)
plt.xlabel("average unemployment rate (%)")
plt.title("Average unemployment rate by state")
plt.tight_layout()
plt.savefig("outputs/by_region.png")
plt.close()

# how much each state went up after covid started
change = df.pivot_table(index="Region", columns="period", values="rate")
change["increase"] = change["covid"] - change["before covid"]
print(change.sort_values("increase", ascending=False).head(10))
change.to_csv("outputs/region_change.csv")

# rural vs urban
print(df.groupby("Area")["rate"].mean())
plt.figure(figsize=(10, 5))
sns.lineplot(data=df, x="Date", y="rate", hue="Area", errorbar=None)
plt.axvline(lockdown, color="red", linestyle="--")
plt.title("Rural vs urban unemployment rate")
plt.ylabel("unemployment rate (%)")
plt.savefig("outputs/rural_urban.png")
plt.close()

# month wise average, only before covid so the spike doesn't hide it
# (only one year of data, so this is not a proper seasonal pattern)
before = df[df["period"] == "before covid"]
month_avg = before.groupby("month")["rate"].mean()
print(month_avg)
month_avg.plot(kind="bar")
plt.title("Average rate by month (before covid)")
plt.ylabel("average rate (%)")
plt.xlabel("month")
plt.savefig("outputs/month_wise.png")
plt.close()

# labour participation vs unemployment
print(df[["participation", "rate"]].corr())
sns.scatterplot(data=df, x="participation", y="rate", hue="period")
plt.title("Labour participation vs unemployment")
plt.savefig("outputs/participation.png")
plt.close()

print("highest month:", monthly.idxmax().date(), round(monthly.max(), 2))
