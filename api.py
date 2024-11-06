import requests

# Create a session object
session = requests.Session()
url = "https://abf0-2401-4900-838f-e94a-2480-70c4-7f15-9e98.ngrok-free.app/"

try:
    # Example for creating a session
    response = session.post(url + 'create_session/')
    response.raise_for_status()  # Check for HTTP errors
    print(response.json())

    query_data = {
    "query": "Find highly-rated restaurants near my current location at Latitude: 28.6542, Longitude: 77.2373. Return a list of restaurants including each one's name, location, rating, and cuisine type in JSON format."
}
    response = session.post(url + 'submit_query/', json=query_data)
    response.raise_for_status()   # Check for HTTP errors
    print(response.json())

except requests.exceptions.RequestException as e:
    print("An error occurred:", e)