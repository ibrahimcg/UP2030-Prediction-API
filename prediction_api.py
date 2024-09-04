import requests

class PredictionAPI:
    def __init__(self, api_url, api_token):
        self.api_url = api_url
        self.api_token = api_token

    def predict(self, targets, target_year, data):
        if not targets:
            raise ValueError("No prediction targets specified")

        headers = {"Authorization": self.api_token}
        payload = {
            "target_features": targets,
            "target_year": target_year,
            "data": data if isinstance(data, list) else [data]
        }
        response = requests.post(self.api_url, json=payload, headers=headers)
        
        if response.status_code == 200:
            return response.json()
        
        else:
            raise Exception(f"Error: {response.status_code}, {response.text}")