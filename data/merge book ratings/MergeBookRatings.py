import pandas as pd

books_df = pd.read_csv("BX-Books.csv")
ratings_df = pd.read_csv("BX-Ratings.csv")

merged_bookratings = pd.merge(ratings_df, books_df, on='ISBN', how='inner')

merged_bookratings.to_csv("BX-MergedBookRatings.csv", index=False)