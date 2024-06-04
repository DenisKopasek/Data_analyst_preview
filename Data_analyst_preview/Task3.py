import pandas as pd
import os

# Load the data
current_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(current_dir, 'Data Analyst Take Home Exam Data.csv')
data = pd.read_csv(data_path)


# Filter data for Tech and Markets sections
tech_data = data[data['section'] == 'WSJ_Tech']
markets_data = data[data['section'] == 'WSJ_Markets']

# Calculate the pageviews for each section
tech_pageviews = tech_data.shape[0]
markets_pageviews = markets_data.shape[0]

# Calculate the number of people who returned for each section
tech_returned = tech_data['secondVisitDate'].notna().sum()
markets_returned = markets_data['secondVisitDate'].notna().sum()

# Calculate the return rate for each section
tech_return_rate = round(tech_returned / tech_data['customerID'].nunique() * 100, 2)
markets_return_rate = round(markets_returned / markets_data['customerID'].nunique() * 100, 2)

print(f"Number of First-time visitors of Tech section: {tech_pageviews}, with {tech_returned} returning visitors, representing a return rate of: {tech_return_rate}%")
print(f"Number of First-time visitors of Markets section: {markets_pageviews}, with {markets_returned} returning visitors, representing a return rate of: {markets_return_rate}%")
