import json
import os

def json_to_dat(json_data, output_file):
    # Ensure the output file is created if it doesn't exist
    if not os.path.exists(output_file):
        open(output_file, 'w').close()

    # Open the .dat file in append mode to write data
    with open(output_file, 'a') as file:
        # Iterate through each record in the JSON data (assuming it's a list of dictionaries)
        for record in json_data:
            # Create a string with '|' separating the values
            line = '|'.join(str(record[key]) for key in record)
            # Write the line to the file
            file.write(line + '\n')

# Example JSON data from an API response (replace this with your API data)
json_data = [
    {"name": "John Doe", "age": 30, "email": "john@example.com"},
    {"name": "Jane Smith", "age": 25, "email": "jane@example.com"}
]

# Convert the JSON data to a .dat file
output_file = "output.dat"
json_to_dat(json_data, output_file)

print(f"Data written to {output_file}")
