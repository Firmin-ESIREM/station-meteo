import requests
import random
import time

while True:
	r = requests.post("http://127.0.0.1:1234/add_data/", data={"temperature": random.uniform(-10.0, 45.0), "humidity": random.uniform(0.0, 100.0), "pressure": random.uniform(9500.0, 10500.0), "air_quality": random.randint(0, 3)})
	print(r.status_code)
	time.sleep(10)
