# User-Data-Analysis-with-Plotly
This repository contains an exploratory data analysis (EDA) of a user dataset(1.3m users)  using **Python**, **Pandas**, and **Plotly Express**. The dataset includes user-level information such as follower count, following count, account creation time, and social media handles.
## 🗂 Dataset

- **Filename:** `user.csv`
- **Fields used in analysis:**
  - `username`
  - `num_followers`
  - `num_following`
  - `instagram`
  - `twitter`
  - `invited_by_user_profile`
  - `time_created`

## 📈 Visualizations and Descriptions

### 1. Distribution of Followers
```python
fig = px.histogram(df, x='num_followers', title='Distribution of Followers', nbins=30)
```
- A histogram showing how followers are distributed across all users.
- Helps identify whether most users have few followers or if there's a large range.

### 2. Distribution of Following
```python
fig = px.histogram(df, x='num_following', title='Distribution of Following', nbins=30)
```
- Similar to the followers histogram, this plot shows how many accounts users typically follow.

### 3. Scatter Plot: Followers vs Following
```python
fig = px.scatter(df, x='num_following', y='num_followers', ...)
```
- Visualizes the relationship between the number of users someone follows and how many followers they have.
- Useful for spotting influential users or outliers.

### 4. Pie Chart: Invited By User Profile
```python
fig = px.pie(df, values='num_followers', names='invited_by_user_profile', ...)
```
- Shows which users invited the most followed members.
- Helps identify top influencers or early adopters.

### 5. Time Series: Account Creation Over Time
```python
df['time_created'] = pd.to_datetime(df['time_created'], errors='coerce')
df_time = df.dropna(subset=['time_created'])
...
fig = px.line(df_time, x='time_created', y='count', ...)
```
- A line chart that tracks how many accounts were created on each day.
- Reveals trends or spikes in user signups.

### 6. Bar Chart: Top 10 Users by Followers
```python
top_users = df.nlargest(10, 'num_followers')
fig = px.bar(top_users, x='username', y='num_followers', ...)
```
- Highlights the top 10 users with the highest follower counts.
- Useful for identifying key influencers on the platform.

### 7. Bar Chart: Top 10 Users by Following
```python
top_following = df.nlargest(10, 'num_following')
fig = px.bar(top_following, x='username', y='num_following', ...)
```
- Displays users who follow the most other users.
- Often indicates networkers or automated accounts.

### 8. Pie Chart: Top 50 People with the Most Followers
```python
top_50_users = df.nlargest(50, 'num_followers')
fig = px.pie(top_50_users, values='num_followers', names='username', ...)
```
- A pie chart representation of the follower share among the top 50 users.
- Useful to show follower concentration.

## 🚀 How to Run

1. Install dependencies:
   ```bash
   pip install pandas plotly
   ```

2. Run the Python script:
   ```bash
   python analysis.py
   ```

3. Visualizations will pop up in your browser using Plotly’s interactive display.

## 📌 Notes

- `time_created` may contain invalid entries, handled with `errors='coerce'` to ensure robustness.
- This project focuses on visualization only; no advanced modeling is included.

# Download the Data Set Here:
https://www.kaggle.com/code/fahadmehfoooz/clubhouse-eda
