import pandas as pd
import re 

users_df = pd.read_csv("BX-Users.csv")

# Normalise the formatting of age
integer = r'\d*'
def find_int(age):
    match = re.search(integer, str(age))
    match = match.group(0)
    if match != '':
        match = int(match)
    else: 
        match = None
    return match

users_df["User-Age"] = users_df["User-Age"].apply(find_int)

# Imputation of the year of publication
blank_age = users_df["User-Age"]
median_age = blank_age.median()
users_df["User-Age"] = blank_age.fillna(median_age)

users_df.to_csv("BX-Users.csv", index=False)
