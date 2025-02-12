import httpx
from time import sleep

URL = "https://api.example.com/system/metrics"
headers = {"Authorization": "Bearer YOUR_API_KEY"}
params = {"metrics": "cpu,memory"}  

def get_metrics():
    print("Fetching system metrics...")
    retry = 3
    delay = 2
    for i in range(retry):
        try:
            response = httpx.get(URL, params=params, headers=headers)
            code = response.status_code 
            if code == 401:
                print(f"Code {code}. Invalid API Key.")
            elif code == 500:
                print(f"Attempt {i} failed: Server is currently down.")
            break
        except httpx.HTTPError:
            print(f"Attempt {i + 1} failed: Server is currently down.")
            sleep(delay)
            print(f"Retrying in {delay} seconds...")

get_metrics()