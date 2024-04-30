import pandas as pd

newbooks_df = pd.read_csv("BX-NewBooks.csv")

# Imputation of the year of publication
raw_year = newbooks_df["Year-Of-Publication"]
min_year = 999
next_year = 2025
real_year = raw_year.loc[(raw_year > min_year) & (raw_year < next_year)]
median_year = real_year.median()
newbooks_df["Year-Of-Publication"].loc[(raw_year <= min_year) | (raw_year >= next_year)] = median_year

newbooks_df.to_csv("BX-NewBooks.csv", index=False)