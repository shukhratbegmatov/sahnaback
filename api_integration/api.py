# api_integration/api.py
import requests

def get_api_data():
    url = "https://sahna.multibot.uz/api"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an exception for HTTP errors

        data = response.json()  # Assuming the response is in JSON format
        return data
    except requests.exceptions.RequestException as e:
        # Handle any request exceptions
        print("Error fetching data:", e)
        return None
