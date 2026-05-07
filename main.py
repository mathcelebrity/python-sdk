
---

# 🐍 2. Python SDK

### `mathcelebrity.py`
```python id="o3v6kj"
import requests

class MathCelebrityAPI:
    def __init__(self, api_key, base_url="https://api.mathcelebrity.com"):
        self.api_key = api_key
        self.base_url = base_url

    def _request(self, endpoint, data=None):
        url = f"{self.base_url}/{endpoint}"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        response = requests.post(url, json=data or {}, headers=headers)

        if response.status_code != 200:
            raise Exception(f"API Error: {response.status_code}")

        return response.json()

    def solve(self, problem):
        return self._request("solve", {"problem": problem})

    def quiz(self, options=None):
        return self._request("quiz", options or {})

    def random(self):
        return self._request("random")

      def sudoku(self):
        return self._request("sudoku")
