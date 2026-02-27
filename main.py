import json
from datetime import datetime
from tripdata import get_trip

# Create list of trips
trips = []

trips.append(get_trip("Paris", "15-05-2023", "Beautiful city!"))
trips.append(get_trip("Tokyo", "10-09-2022", "Amazing culture"))
trips.append(get_trip("New York", "01-01-2024", "Great New Year celebration"))

# Convert date string to date object and format it
for trip in trips:
    # Convert string to date object
    date_object = datetime.strptime(trip["date"], "%d-%m-%Y")
    
    # Format date as "Month Day, Year"
    formatted_date = date_object.strftime("%B %d, %Y")
    
    # Update dictionary
    trip["date"] = formatted_date

# Convert list to JSON string
json_data = json.dumps(trips, indent=4)

print(json_data)