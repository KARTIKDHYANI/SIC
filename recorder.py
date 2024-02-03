import time
from datetime import datetime
from CSVHandler import CSVHandler  # Assuming CSVHandler is defined in CSVHandler.py
from moisture import moist  # Assuming moisture class is defined in moisture.py
m=moist()
while True:
    
    ob1 = CSVHandler('Data.csv', 'Time', 'Moisture level')

    ob1.insert_data((datetime.now().strftime("%H:%M"),m.get_moisture_data() ))
    time.sleep(60)
    ob1.insert_data((datetime.now().strftime("%H:%M"),m.get_moisture_data()))
    time.sleep(60)
    ob1.insert_data((datetime.now().strftime("%H:%M"),m.get_moisture_data() ))
    time.sleep(60)
    ob1.insert_data((datetime.now().strftime("%H:%M"), m.get_moisture_data()))
    time.sleep(60)
    ob1.insert_data((datetime.now().strftime("%H:%M"),m.get_moisture_data() ))
    time.sleep(60)

    ob1.plot_data()
    ob1.clear_data()
    






