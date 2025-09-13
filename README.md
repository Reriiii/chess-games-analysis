# Chess Games Analysis

## 📌 Dataset
- **Source:** [Lichess Database](https://database.lichess.org/)  
- **Sampling Method:** Reservoir Sampling (1M games/month)  
- **Period:** 09/2024 – 08/2025  
- **Size:** 12,000,000 rows × 10 columns  
- **Features:** 
    - **Event**: Tournament or type of event (e.g., rated blitz, arena, match)  
    - **Date**: Date of the game  
    - **White_Name**: Username of the player with the white pieces  
    - **Black_Name**: Username of the player with the black pieces  
    - **WhiteElo**: Elo rating of the white player before the game  
    - **BlackElo**: Elo rating of the black player before the game  
    - **WhiteRatingDiff**: Rating change of the white player after the game (+/-)  
    - **BlackRatingDiff**: Rating change of the black player after the game (+/-)  
    - **Result**: Outcome of the game (`1-0` white wins, `0-1` black wins, `1/2-1/2` draw)  
    - **Opening**: Chess opening name (based on ECO classification)  
    - **TimeControl**: Time control format (e.g., `300+0` = 5 min, `600+5` = 10 min + 5 sec increment)  


---

## 1. Business Understanding and Analytic Approach
- **Goals:**
  - Analyze online chess behavior (skill level, openings, results, time controls).  
  - Identify trends: Most popular openings, win rates across different time controls.  
  - Compare strategies of higher-rated vs lower-rated players.  

- **Focus Areas:**
  - **Player-based:** Ratings, win rate, white vs black performance.  
  - **Game-based:** Length of games, opening choices, time control.  
  - **Trend-based:** Monthly shifts in behavior.  

---

## 2. Data Collection, Understanding, Preparation
- **Collection:**
  - Download PGN data from Lichess (monthly dumps).  
  - Apply sampling (1M games per month).  

- **Cleaning:**
  - Remove games with missing metadata.  
  - Convert timestamps to `datetime`.  
  - Normalize ratings (`int` type).  
  - Map results (`1-0 → White Win`, `0-1 → Black Win`, `½-½ → Draw`).  

---

## 3. Data Analysis with SQL

After preprocessing, the dataset will be imported into **PostgreSQL** for structured querying.

### Goals
- Count and validate the total number of sampled games.  
- Explore player performance statistics.  
- Analyze the popularity of different chess openings.  
- Study rating distributions across different time periods.  
- Identify patterns in results (win, loss, draw) by Elo ranges and time controls.  


## 4. Data Analysis with Python

- Load the sampled dataset `(12,000,000 rows × 10 features)` into Pandas for exploration.  
- Perform feature understanding:
  - **Player Ratings**: Analyze rating distributions of White and Black.  
  - **Result Patterns**: Compare win/draw/loss frequencies across rating levels.  
  - **TimeControl Impact**: Group by time control formats (e.g., Blitz, Rapid, Classical).  
  - **Openings**: Identify the most common openings and their success rates.  
- Use Matplotlib/Seaborn for visualization:
  - Rating histograms, result distributions, and opening popularity trends.  
  - Line plots of average rating per month (Sept 2024 – Aug 2025).  

## 5. Data Visualization

- Create dashboards and visual summaries:  
  - **Win Rate by Elo Range**: Compare different rating brackets.  
  - **Top 10 Openings**: Show usage frequency and success rate.  
  - **Monthly Trends**: Games played per month across time controls.  
- Use heatmaps and bar charts for clear insights.  

## 6. Regression and Predictive Modeling

- Objective: Predict **game outcome (Result)** using features.  
- Possible models:
  - Logistic Regression (predict win/draw/loss).  
  - Decision Trees / Random Forests (feature importance on Elo, Opening, TimeControl).  
- Evaluate models with accuracy and F1-score.  

## 7. Data Analysis with Tools

- Load the processed dataset into **SQL** for query-based analysis:  
  - Example: Find games where rating difference > 500.  
  - Example: Count games by TimeControl and Opening.  
- Build interactive dashboards with **Power BI** or **Tableau**:  
  - Win rate distribution by Elo range.  
  - Opening effectiveness comparison.  
  - Monthly game activity trends.  

---
