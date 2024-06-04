import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load the data
current_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(current_dir, 'Data Analyst Take Home Exam Data.csv')
data = pd.read_csv(data_path)


# 'firstVisitDate' to datetime format
data['firstVisitDate'] = pd.to_datetime(data['firstVisitDate'])

# Extract just the date part of 'firstVisitDate'
data['visitDate'] = data['firstVisitDate'].dt.date



# Group data by visitDate and section, and count the number of first-time visits
visitor_counts = data.groupby(['visitDate', 'section']).size().reset_index(name='visitors')

# Sorting the dates
visitor_counts = visitor_counts.sort_values('visitDate')

# Pivot the data to get sections as columns and dates as rows
visitor_pivot = visitor_counts.pivot(index='visitDate', columns='section', values='visitors').fillna(0)

# Create a stacked bar plot with a more distinguishable colormap
ax = visitor_pivot.plot(kind='bar', stacked=True, figsize=(14, 8), colormap='tab20')

# Set plot title and labels
plt.title('Number of First-Time Visits by Section for Each Date (Stacked)')
plt.xlabel('Date')
plt.ylabel('Number of First-Time Visits')
plt.xticks(rotation=45)

# Adjust the legend to be within the plot
plt.legend(title='Section', loc='upper right', ncol=1)
plt.tight_layout()

# Show the plot
plt.show()

#Graph "Number of First-Time Visits per Day"

# Group data by visitDate and count the number of first-time visits
visits_per_day = data.groupby('visitDate').size()

# Plot the line graph
plt.figure(figsize=(14, 8))
visits_per_day.plot(kind='line', marker='o', color='blue')

# Set plot title and labels
plt.title('Number of First-Time Visits per Day')
plt.xlabel('Date')
plt.ylabel('Number of First-Time Visits')
plt.xticks(rotation=45)

# Show the plot
plt.tight_layout()
plt.show()

#Graph "Number of First-Time Visits by Section Individually for Each Date"

# Ensure 'firstVisitDate' is in datetime format
data['firstVisitDate'] = pd.to_datetime(data['firstVisitDate'])

# Extract just the date part of 'firstVisitDate'
data['visitDate'] = data['firstVisitDate'].dt.date

# Group data by visitDate and section, and count the number of first-time visits
visitor_counts = data.groupby(['visitDate', 'section']).size().reset_index(name='visitors')

# Ensure dates are sorted
visitor_counts = visitor_counts.sort_values('visitDate')

# Set the figure size
plt.figure(figsize=(14, 8))

# Create a bar plot
sns.barplot(data=visitor_counts, x='visitDate', y='visitors', hue='section')

# Set plot title and labels
plt.title('Number of First-Time Visits by Section Individually for Each Date')
plt.xlabel('Date')
plt.ylabel('Number of First-Time Visits')
plt.xticks(rotation=45)
plt.legend(title='Section')
plt.tight_layout()

# Show the plot
plt.show()
