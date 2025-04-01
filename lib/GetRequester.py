import requests

class GetRequester:
    def __init__(self, url):
        # Initialize with the URL
        self.url = url

    def get_response_body(self):
        # Sends GET request and returns the body of the response
        try:
            response = requests.get(self.url)
            response.raise_for_status()  # Raises an error for bad status codes (4xx, 5xx)
            return response.text  # Returns the raw body of the response
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None

    def load_json(self):
        # Calls get_response_body and converts the response to JSON
        response_body = self.get_response_body()
        if response_body:
            return requests.get(self.url).json()  # Convert the JSON data to a Python dictionary/list
        return None
