import csv
from moisture import moist
from stat_1 import stat
from datetime import datetime
import time
s=stat()
m=moist()
while True:

    # Open the CSV file in read mode
    with open('irrigation_data.csv', 'r', newline='') as csvfile:
        # Create a CSV reader object
        reader = csv.DictReader(csvfile)
        
        # Extract data from the first row (should be only one row)
        for row in reader:
            # Convert extracted data to integers
            irrigation_hour = int(row['irrigation_hour'])
            irrigation_minute = int(row['irrigation_minute'])
            water_flow_time = int(row['water_flow_time'])

    # Get the current time
    current_time = datetime.now()
    current_hour = int(current_time.hour)
    current_minute = int(current_time.minute)
    
    # Compare irrigation hour and minute with current hour and minute
    if irrigation_hour == current_hour and irrigation_minute == current_minute and m.get_moisture_data()<80:
        print(True)
        s.poststat(1)
        time.sleep(water_flow_time*60)
        s.poststat(0)
    
