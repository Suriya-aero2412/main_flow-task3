import csv

# Open the CSV file
with open('/01.Data Cleaning and Preprocessing.csv', 'r') as file:
    # Create a CSV reader object
    reader = csv.reader(file)

    # Iterate over the rows in the CSV file
    for row in reader:
        print(row)
        import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('/01.Data Cleaning and Preprocessing.csv')

# Display the first few rows
print(df.head())
# Filter the DataFrame to only include rows where the 'age' column is greater than 30
filtered_df = df[df['age'] > 30]
print(filtered_df)
# Group the DataFrame by the 'department' column and calculate the average 'salary'
grouped_df = df.groupby('department')['salary'].mean()
print(grouped_df)
# Sort the DataFrame by the 'name' column in ascending order
sorted_df = df.sort_values('name')
print(sorted_df)
