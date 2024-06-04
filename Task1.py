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

print(f"Percentage of customers who returned after the first visit: {percentage_returned:.1f}%")