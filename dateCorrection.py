import csv
import pandas as pd

# # Open the input and output CSV files
# with open('books_info.csv', 'r') as input_file, open('books_info_updated.csv', 'w', newline='') as output_file:
#     reader = csv.DictReader(input_file)
#     writer = csv.DictWriter(output_file, fieldnames=reader.fieldnames)
#     writer.writeheader()

#     # Iterate over each row in the input CSV file
#     for row in reader:
#         # Check if the "date" column contains a range of years separated by "-"
#         if '-' in row['date']:
#             # Split the range of years into two separate years
#             start_year, end_year = row['date'].split('-')
#             # Iterate over each year in the range and create a new row for each year
#             for year in range(int(start_year), int(end_year)+1):
#                 # Create a new row with the same data as the original row, except for the "date" column
#                 new_row = row.copy()
#                 new_row['date'] = str(year)
#                 # Write the new row to the output CSV file
#                 writer.writerow(new_row)
#         else:
#             # If the "date" column does not contain a range of years, write the original row to the output CSV file
#             writer.writerow(row)

# df = pd.read_csv('books_info_updated.csv')


# # Drop all rows with Null values in date col
# df = df.dropna(subset=['date'])

# # Write the updated DataFrame to a new CSV file
# df.to_csv('books.csv', index=False)


# df = pd.read_csv('books.csv')

# # Remove the last two characters from the 'data' column
# df['date'] = df['date'].astype(str).str[:-2]

# # Write the updated DataFrame to a new CSV file
# df.to_csv('books_2.csv', index=False)


# import csv
# # Open the CSV file and read its contents as a list of dictionaries
# with open('books_2.csv') as csvfile:
#     reader = csv.DictReader(csvfile)
#     rows = [row for row in reader]
# # Loop over each row and check if its date column equals '191'
# for row in rows:
#     if row['date'] == '18':  # replace 'date' with your actual date column name
#         print(row)  # or do something else with this matching row data


# read the original CSV file
# df = pd.read_csv('books_2.csv')

# # remove any row where the date column does not contain a 4-digit integer year
# df = df.dropna(subset=['date']) # Drop rows with missing values if any
# df = df[pd.to_numeric(df['date'], errors='coerce').notnull()] # Drop rows where the date_column column cannot be converted to a numeric format
# df = df[df['date'].astype(int) // 10000 == 0] # Select only rows where the date_column column represents a year with 4 digit in int format.

# # write the clean data to a new CSV file
# df.to_csv('clean_data.csv', index=False)


# import csv

# list= ['18','19','190','191','192','193','194','195','196','197','198','199']
# # Open the input CSV file and read its contents as a list of dictionaries
# with open('output.csv') as csvfile:
#     reader = csv.DictReader(csvfile)
#     rows = [row for row in reader]
# # Create a list to store all non-matching rows
# new_rows = []
# # Loop over each row and check if its date column equals '18'
# for row in rows:
#     for item in list: 
#         if row['date'] == item:  # replace 'date' with your actual date column name
#             print(f"Removing matching row: {row}")
#         else:
#             new_rows.append(row)
# # Write the non-matching rows to a new CSV file called "output.csv"
# with open('final.csv', mode='w', newline='') as output_file:
#     fieldnames = ["title","url","contributors","date","format","fulltext_url","trove_id","language","rights","pages",
#                   "form","volume","parent","children","text_downloaded","text_file"]
#     writer = csv.DictWriter(output_file, fieldnames=fieldnames)
#     writer.writeheader()  # write header row first
#     for row in new_rows:
#         writer.writerow(row)


import pandas as pd

list= ['18','19','190','191','192','193','194','195','196','197','198','199']
# Read the input CSV file into a pandas DataFrame
df = pd.read_csv('output.csv')

# Create a boolean mask for rows where the date column does not match the list
mask = ~df['date'].isin(list)

# Get the non-matching rows
new_df = df[mask]

# Create a new CSV file with the non-matching rows
new_df.to_csv('final.csv', index=False)

print(f"{len(df) - len(new_df)} matching rows were removed and {len(new_df)} rows were written to 'final.csv' file.")
