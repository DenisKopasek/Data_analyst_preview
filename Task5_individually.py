import pandas as pd
import matplotlib.pyplot as plt
import os

# Load the data
current_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(current_dir, 'Data Analyst Take Home Exam Data.csv')
data = pd.read_csv(data_path)


# Ensure 'firstVisitDate' is in datetime format
data['firstVisitDate'] = pd.to_datetime(data['firstVisitDate'])

# Extract just the date part of 'firstVisitDate'
data['visitDate'] = data['firstVisitDate'].dt.date

# Group data by visitDate, articleID, headline, and section, then count the number of visits for each article on each day
daily_visits = data.groupby(['visitDate', 'articleID', 'headline', 'section']).size().reset_index(name='visits')

# Find the most visited article for each day
most_visited_per_day = daily_visits.loc[daily_visits.groupby('visitDate')['visits'].idxmax()]

# Select the relevant columns
most_visited_info = most_visited_per_day[['visitDate', 'headline', 'section', 'visits']]

# Display the top article for each day in the console
print(most_visited_info)

# Save the most visited articles data to an Excel file
output_path = os.path.join(current_dir, 'most_visited_articles_per_day.xlsx')
most_visited_info.to_excel(output_path, index=False)

print(f"Top articles have been exported to {output_path}")

# Plotting
plt.figure(figsize=(12, 6))
plt.bar(most_visited_per_day['visitDate'], most_visited_per_day['visits'], color='skyblue')
plt.title('Most Visited Article per Day')
plt.xlabel('Date')
plt.ylabel('Number of Visits')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
