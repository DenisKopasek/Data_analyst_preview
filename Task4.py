import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load the data
current_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(current_dir, 'Data Analyst Take Home Exam Data.csv')
data = pd.read_csv(data_path)


#Graph "Return Rate by Section"


# Calculate the return rate for each section
section_return_rate = data.groupby('section')['secondVisitDate'].apply(lambda x: x.notna().mean()).reset_index(name='return_rate')
section_return_rate['return_rate'] *= 100 

max_return_rate = section_return_rate['return_rate'].max()
min_return_rate = section_return_rate['return_rate'].min()
print(f"Maximum return rate: {max_return_rate:.1f}")
print(f"Minimum return rate: {min_return_rate:.1f}")

# Plot the return rate for each section
plt.figure(figsize=(14, 8))
sns.set(style="whitegrid")

# Create bar plot
ax = sns.barplot(data=section_return_rate, x='section', y='return_rate', hue='section', palette='viridis', legend=False)

# Set title and labels with consistent font size
plt.title('Return Rate by Section', fontsize=16)
plt.xlabel('Section', fontsize=14)
plt.ylabel('Return Rate (%)', fontsize=14)

# Rotate x-axis labels and set font size
plt.xticks(rotation=45, ha='right', fontsize=12)

# Set y-axis labels font size
plt.yticks(fontsize=12)

# Set y-axis limits to ensure consistent sizing
plt.ylim(0, section_return_rate['return_rate'].max() * 1.1)  # Add a little extra space for aesthetics

# Adjust layout to ensure everything fits
plt.tight_layout()

# Further adjust subplots if necessary
plt.subplots_adjust(bottom=0.2)

# Show plot
plt.show()


#Graph "Return Rate by Word Count"


# Calculate the return rate for each word count
word_count_return_rate = data.groupby('wordCount')['secondVisitDate'].apply(lambda x: x.notna().mean()).reset_index(name='return_rate')

# Calculate correlation coefficient
correlation = word_count_return_rate['wordCount'].corr(word_count_return_rate['return_rate'])
print(f"Correlation coefficient between word count and return rate: {correlation:.2f}")

# Plot the relationship between word count and return rate
plt.figure(figsize=(12, 6))
sns.scatterplot(data=word_count_return_rate, x='wordCount', y='return_rate')
plt.title('Return Rate by Word Count')
plt.xlabel('Word Count')
plt.ylabel('Return Rate')
plt.show()


#Graph "Return Rate by Word Count with Regression Line'"


# Plot the relationship with a regression line
plt.figure(figsize=(12, 6))
sns.scatterplot(data=word_count_return_rate, x='wordCount', y='return_rate')
sns.regplot(data=word_count_return_rate, x='wordCount', y='return_rate', scatter=False, color='red')
plt.title('Return Rate by Word Count with Regression Line')
plt.xlabel('Word Count')
plt.ylabel('Return Rate')
plt.show()
