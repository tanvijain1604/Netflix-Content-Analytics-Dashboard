# Netflix Content Analytics Dashboard

## Project Overview

The Netflix Content Analytics Dashboard is a data analysis project developed using Python. The project analyzes Netflix's content library to uncover trends related to movies, TV shows, ratings, genres, countries, and content growth over time.

The project demonstrates the use of NumPy, Pandas, Matplotlib, and Seaborn for data cleaning, analysis, and visualization.

---

## Objectives

- Perform data cleaning and preprocessing.
- Analyze Netflix content distribution.
- Compare Movies and TV Shows.
- Identify top content-producing countries.
- Analyze ratings and genres.
- Study Netflix's content growth over the years.
- Generate meaningful insights through visualizations.

---

## Technologies Used

- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn

---

## Dataset

Dataset: Netflix Movies and TV Shows Dataset

The dataset contains information such as:

- Title
- Type (Movie/TV Show)
- Director
- Cast
- Country
- Release Year
- Date Added
- Rating
- Duration
- Genre
- Description

---

## Features

### 1. Data Cleaning
- Handles missing values.
- Converts date columns into proper datetime format.
- Creates a new Year Added column.

### 2. NumPy Analysis
- Average release year.
- Oldest release year.
- Latest release year.

### 3. Movies vs TV Shows Analysis
- Compares the number of Movies and TV Shows available on Netflix.

### 4. Ratings Analysis
- Displays the distribution of content ratings.

### 5. Country Analysis
- Identifies the top countries producing Netflix content.

### 6. Genre Analysis
- Finds the most common genres on Netflix.

### 7. Netflix Growth Analysis
- Visualizes the number of titles added over the years.

---

## Visualizations Generated

### Movies vs TV Shows
Bar chart showing content type distribution.

### Ratings Distribution
Count plot of content ratings.

### Top Countries
Bar chart of the top 10 content-producing countries.

### Netflix Growth Over Time
Line graph showing content additions by year.

### Top Genres
Bar chart showing the most popular genres.

---

## Project Workflow

1. Import required libraries.
2. Load Netflix dataset.
3. Handle missing values.
4. Convert date columns.
5. Perform exploratory data analysis.
6. Generate visualizations.
7. Extract insights from the dataset.

---

## Sample Insights

- Movies significantly outnumber TV Shows.
- Netflix experienced rapid content growth after 2015.
- Certain countries contribute the majority of Netflix content.
- TV-MA is among the most common ratings.
- International Movies and Dramas are highly represented genres.

---

## How to Run the Project

### Step 1: Install Dependencies

```bash
pip install pandas numpy matplotlib seaborn
```

### Step 2: Place Dataset

Place `netflix_titles.csv` in the project folder.

### Step 3: Run the Program

```bash
python netflix_analysis.py
```

---

## Output

The project generates:

- Statistical summaries
- Data insights
- Visual graphs
- PNG image files for each visualization

---

## Learning Outcomes

Through this project, I learned:

- Data preprocessing using Pandas
- Numerical analysis using NumPy
- Data visualization using Matplotlib and Seaborn
- Exploratory Data Analysis (EDA)
- Extracting business insights from real-world datasets

---

## Future Enhancements

- Interactive dashboard using Streamlit
- Machine Learning-based content prediction
- Recommendation system
- Genre trend forecasting

---
