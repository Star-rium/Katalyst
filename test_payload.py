import time
import requests

BRIDGE_URL = "http://localhost:50005/state"

def verify_bridge():
    print("Pinging C# Game Bridge...")
    while True:
        try:
            start_t = time.perf_counter()
            response = requests.get(BRIDGE_URL, timeout=1.0)
            latency_ms = (time.perf_counter() - start_t) * 1000
        
            if response.status_code == 200:
                data = response.json()
                print(f"OK ({latency_ms:.1f}ms))", data)
            else:
                print(f"Server error: {response.status_code}")
            time.sleep(0.2)
        except requests.exceptions.RequestException as e:
            print(f"Connection failed: {e}")
            time.sleep(0.5)
        
        
if __name__ == "__main__":
    verify_bridge()