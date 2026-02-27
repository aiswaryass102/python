import json
from datetime import datetime
from tracker import create_record

# Create list of travel records
records = []

records.append(create_record("London", "Amazing trip!", "05-06-2022"))
records.append(create_record("Rome", "Loved the history.", "12-08-2023"))
records.append(create_record("Sydney", "Beautiful beaches.", "20-01-2024"))

# Convert date format
for record in records:
    date_object = datetime.strptime(record["date"], "%d-%m-%Y")
    formatted_date = date_object.strftime("%B %d, %Y")
    record["date"] = formatted_date

# Convert list to JSON string
json_data = json.dumps(records, indent=4)
print("JSON Data:")
print(json_data)

# Parse JSON back to Python object
parsed_data = json.loads(json_data)

print("\nTravel Records:")
for item in parsed_data:
    print(item["city"], "-", item["comment"], "-", item["date"])