0
import requests
# ESP32 IP address
esp32_ip = "192.168.4.1"  # Replace with the actual IP address of your ESP32
# Define the endpoint for updating status
status_endpoint = f"http://{esp32_ip}/status"
# New status value to set
new_status = int(input('Enter status'))
# Send POST request to update status
response = requests.post(status_endpoint, data={"value":str(new_status)})
#Check if the request was successful
if response.status_code == 200:
    print("Status updated successfully")
else:
    print(f"Failed to update status. Status code: {response.status_code}")