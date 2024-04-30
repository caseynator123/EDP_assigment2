import pandas as pd

books_df = pd.read_csv("BX-Books.csv")

# Imputation of the year of publication
raw_year = books_df["Year-Of-Publication"]
min_year = 999
next_year = 2025
real_year = raw_year.loc[(raw_year > min_year) & (raw_year < next_year)]
median_year = real_year.median()
books_df["Year-Of-Publication"].loc[(raw_year <= min_year) | (raw_year >= next_year)] = median_year

books_df.to_csv("BX-Books.csv", index=False)