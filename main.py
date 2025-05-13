import pandas as pd
import plotly.express as px

# Load the dataset
df = pd.read_csv('user.csv')
print(df.head())  # Display the first few rows of the dataset

# 1. Distribution of Followers (Histogram)
fig = px.histogram(df, x='num_followers', title='Distribution of Followers', nbins=30)
fig.show()

# 2. Distribution of Following (Histogram)
fig = px.histogram(df, x='num_following', title='Distribution of Following', nbins=30)
fig.show()

# 3. Scatter Plot: Followers vs Following
fig = px.scatter(df, x='num_following', y='num_followers', title='Followers vs Following', 
                 hover_data=['username', 'twitter', 'instagram'])
fig.show()

# 4. Pie Chart: Invited By User Profile
fig = px.pie(df, values='num_followers', names='invited_by_user_profile', 
             title='Invited By User Profile Distribution')
fig.show()

# 5. Time Series: Account Creation Over Time
# Handle inconsistent datetime formats
df['time_created'] = pd.to_datetime(df['time_created'], errors='coerce')  # Convert to datetime, invalid entries become NaT
df_time = df.dropna(subset=['time_created'])  # Drop rows with invalid dates
df_time = df_time.groupby(df_time['time_created'].dt.date).size().reset_index(name='count')
fig = px.line(df_time, x='time_created', y='count', title='Account Creation Over Time')
fig.show()

# 6. Bar Chart: Top 10 Users by Followers
top_users = df.nlargest(10, 'num_followers')
fig = px.bar(top_users, x='username', y='num_followers', title='Top 10 Users by Followers', 
             hover_data=['twitter', 'instagram'])
fig.show()

# 7. Bar Chart: Top 10 Users by Following
top_following = df.nlargest(10, 'num_following')
fig = px.bar(top_following, x='username', y='num_following', title='Top 10 Users by Following', 
             hover_data=['twitter', 'instagram'])
fig.show()

# 8. Pie Chart: Top 50 People with the Most Followers
top_50_users = df.nlargest(50, 'num_followers')  # Get the top 50 users by followers
fig = px.pie(top_50_users, values='num_followers', names='username', 
             title='Top 50 People with the Most Followers')
fig.show()