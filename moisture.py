import requests
class moist:
     
    def get_moisture_data():
        esp32_ip = "192.168.4.1"
        try:
            response = requests.get(f"http://{esp32_ip}/moisture")
            if response.status_code == 200:
                return int(response.text)
            else:
                print(f"Error: {response.status_code} - {response.text}")
                return None
        except requests.exceptions.RequestException as e:
            print(f"Request error: {e}")
            return None
