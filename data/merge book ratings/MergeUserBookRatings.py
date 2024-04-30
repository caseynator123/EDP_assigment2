import pandas as pd

books_df = pd.read_csv("BX-Books.csv")
ratings_df = pd.read_csv("BX-Ratings.csv")
users_df = pd.read_csv("BX-Users.csv")

merged_bookratings = pd.merge(ratings_df, books_df, on='ISBN', how='inner')
merged_userbookratings = pd.merge(merged_bookratings, users_df, on='User-ID', how='inner')

merged_userbookratings.to_csv("BX-MergedUserBookRatings.csv", index=False)