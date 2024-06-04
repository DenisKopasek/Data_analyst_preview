import pandas as pd
import os

# Load the data
current_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(current_dir, 'Data Analyst Take Home Exam Data.csv')
data = pd.read_csv(data_path)


# Calculate the number of customers who returned
returned_customers = data['secondVisitDate'].notna().sum()

# Calculate the total number of customers
total_customers = data['customerID'].nunique()

# Calculate the percentage of customers who returned
percentage_returned = (returned_customers / total_customers) * 100
print(f"Percentage of customers who returned after the first visit: {percentage_returned:.2f}%")

# Function to extract headline
def extract_headline(headline):
    if "_" in headline:
        return headline.split('_')[-1]
    return headline

# Apply the function to the 'headline' column
data['Headline'] = data['headline'].apply(extract_headline)

# Display the first few rows to verify the extraction
print(data[['headline', 'Headline']].head())

# Count Pageviews for each article in each Section
article_views = data.groupby(['section', 'articleID', 'Headline']).size().reset_index(name='Pageviews')

# Find the top three articles in each Section by Pageviews
top_articles = article_views.groupby('section').apply(lambda x: x.nlargest(3, 'Pageviews')).reset_index(drop=True)

# Select the columns to be exported
top_articles_selected_columns = top_articles[['section', 'Headline', 'Pageviews']]

# Print the selected columns
print("Top three best-performing stories in each Section by Pageviews:")
print(top_articles_selected_columns)

# Export to Excel
output_path = os.path.join(current_dir, 'top_articles_by_section.xlsx')
top_articles_selected_columns.to_excel(output_path, index=False)

print(f"Top articles have been exported to {output_path}")
