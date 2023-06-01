import pandas as pd
import csv

# task 1 -> seperate date range into several rows
# Open the input and output CSV files
with open('books_info.csv', 'r') as input_file, open('books_info_updated.csv', 'w', newline='') as output_file:
    reader = csv.DictReader(input_file)
    writer = csv.DictWriter(output_file, fieldnames=reader.fieldnames)
    writer.writeheader()

    # Iterate over each row in the input CSV file
    for row in reader:
        # Check if the "date" column contains a range of years separated by "-"
        if '-' in row['date']:
            # Split the range of years into two separate years
            start_year, end_year = row['date'].split('-')
            # Iterate over each year in the range and create a new row for each year
            for year in range(int(start_year), int(end_year)+1):
                # Create a new row with the same data as the original row, except for the "date" column
                new_row = row.copy()
                new_row['date'] = str(year)
                # Write the new row to the output CSV file
                writer.writerow(new_row)    
            # row['date'] = str(start_year)
            # writer.writerow(row)
        else:
            # If the "date" column does not contain a range of years, write the original row to the output CSV file
            writer.writerow(row)

# Read the input CSV file into a pandas DataFrame
df = pd.read_csv('books_info_updated.csv')

# task 2 -> drop nulls in date
# Drop all rows with Null values in date col
df = df.dropna(subset=['date'])

# task 3 -> reformat date to "yyyy" instead of "yyyyy.0" 
# Remove the last two characters from the 'data' column
df['date'] = df['date'].astype(str).str[:-2]



# task 3 -> remove wrong date 
list= ['18','19','180','181','182','183','184','185','186','187','188','189' ,'190','191','192','193','194','195','196','197','198','199']

# Create a boolean mask for rows where the date column does not match the list
mask = ~df['date'].isin(list)

# Get the non-matching rows
new_df = df[mask]

# Create a new CSV file with the non-matching rows
new_df.to_csv('final_2.csv', index=False)

print(f"{len(df) - len(new_df)} matching rows were removed and {len(new_df)} rows were written to 'final.csv' file.")


