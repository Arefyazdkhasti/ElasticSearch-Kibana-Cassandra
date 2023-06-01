import csv

with open('final_2.csv', 'r') as input_file, open('final_2_formatted.csv', 'w', newline='') as output_file:
    reader = csv.DictReader(input_file)
    writer = csv.DictWriter(output_file, fieldnames=reader.fieldnames)
    writer.writeheader()

    # Iterate over each row in the input CSV file
    for row in reader:
        # Check if the "format" column contains a range of years separated by "-"
        if '|' in row['format']:
            # Split the range of years into two separate years
            formats = row['format'].split('|')

            for format in formats:
                # Create a new row with the same format as the original row, except for the "format" column
                new_row = row.copy()
                new_row['format'] = str(format)
                # Write the new row to the output CSV file
                writer.writerow(new_row)
        else:
            # If the "format" column does not contain a range of years, write the original row to the output CSV file
            writer.writerow(row)