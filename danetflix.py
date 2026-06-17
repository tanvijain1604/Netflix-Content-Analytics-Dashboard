import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ----------------------------
# Load Dataset
# ----------------------------

df = pd.read_csv("netflix_titles.csv")

# ----------------------------
# Data Cleaning
# ----------------------------

df.fillna({
    "director": "Unknown",
    "cast": "Unknown",
    "country": "Unknown",
    "rating": "Unknown",
    "duration": "Unknown",
    "listed_in": "Unknown",
    "description": "Unknown"
}, inplace=True)

df["date_added"] = pd.to_datetime(df["date_added"], errors="coerce")
df["year_added"] = df["date_added"].dt.year

# ----------------------------
# NUMPY ANALYSIS
# ----------------------------

years = np.array(df["release_year"])

print("Average Release Year:", np.mean(years))
print("Oldest Release Year:", np.min(years))
print("Latest Release Year:", np.max(years))

# ----------------------------
# Dataset Summary
# ----------------------------

print("\nDataset Shape:", df.shape)
print("\nMovies and TV Shows:")

print(df["type"].value_counts())

# ----------------------------
# Visualization 1
# Movies vs TV Shows
# ----------------------------

plt.figure(figsize=(6,5))

sns.countplot(data=df,x="type")

plt.title("Movies vs TV Shows")

plt.savefig("movie_tvshow.png")
plt.show()

# ----------------------------
# Visualization 2
# Ratings Distribution
# ----------------------------

plt.figure(figsize=(10,5))

sns.countplot(
    data=df,
    y="rating",
    order=df["rating"].value_counts().index
)

plt.title("Content Ratings")

plt.savefig("ratings.png")
plt.show()

# ----------------------------
# Visualization 3
# Top Countries
# ----------------------------

countries = df["country"].value_counts().head(10)

plt.figure(figsize=(10,6))

sns.barplot(
    x=countries.values,
    y=countries.index
)

plt.title("Top 10 Countries")

plt.savefig("countries.png")
plt.show()

# ----------------------------
# Visualization 4
# Netflix Growth
# ----------------------------

yearly = df["year_added"].value_counts().sort_index()

plt.figure(figsize=(12,5))

sns.lineplot(
    x=yearly.index,
    y=yearly.values,
    marker="o"
)

plt.title("Netflix Content Added Over Time")
plt.xlabel("Year")
plt.ylabel("Number of Titles")

plt.savefig("yearly_growth.png")
plt.show()

# ----------------------------
# Visualization 5
# Top Genres
# ----------------------------

genres = df["listed_in"].str.split(", ").explode()

top_genres = genres.value_counts().head(10)

plt.figure(figsize=(10,6))

sns.barplot(
    x=top_genres.values,
    y=top_genres.index
)

plt.title("Top 10 Genres")

plt.savefig("genres.png")
plt.show()

# ----------------------------
# Insights
# ----------------------------

print("\n----- PROJECT INSIGHTS -----")

print("Most common rating:")
print(df["rating"].mode()[0])

print("\nMost content-producing country:")
print(df["country"].mode()[0])

print("\nMost popular genre:")
print(top_genres.index[0])

print("\nProject Completed Successfully!")