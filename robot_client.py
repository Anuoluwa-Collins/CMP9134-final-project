


import requests


class RobotClient:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(RobotClient, cls).__new__(cls)
            cls._instance.base_url = "http://localhost:5000"
        return cls._instance

    def get_status(self):
        # TODO: implement actual API call
        print("Getting robot status...")
        # response = requests.get(f"{self.base_url}/status")
        # return response.json()

    def move(self, x, y):
        # TODO: implement actual API call
        print(f"Moving robot to ({x}, {y})")
        # response = requests.post(f"{self.base_url}/move", json={"x": x, "y": y})
        # return response.status_code == 200

    def reset(self):
        # TODO: implement actual API call
        print("Resetting robot...")
        # response = requests.post(f"{self.base_url}/reset")
        # return response.status_code == 200