import requests

API_URL = "https://api.nasa.gov/planetary/apod"
API_KEY = "DEMO_KEY"

def get_apod(date=None):
    params = {'api_key': API_KEY}
    if date:
        params['date']= date
    response = requests.get("https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY")
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error fetching APOD: {response.status_code}")