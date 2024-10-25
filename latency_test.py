import requests
import time
import csv
import pandas as pd
import matplotlib.pyplot as plt

url = "http://ece444practical5-env.eba-5cgzpauf.us-east-2.elasticbeanstalk.com/predict"

# real and fake cases
test_cases = {
    "fake_test_1": {"text": "Share a certain post of Bill Gates on Facebook and he will send you money."},
    "fake_test_2": {"text": "A Fargo, North Dakota, man was arrested for clearing snow with a flamethrower."},
    "real_test_1": {"text": "Business groups, opposition parties and the Ontario government react to Trudeau government’s major cut in permanent resident targets."},
    "real_test_2": {"text": "More than 20 lawmakers from his party sign letter asking Canadian prime minister to step down before election"}
}

response_times = {key: [] for key in test_cases}

for test_name, test_data in test_cases.items():
    print(f"Testing: {test_name}")
    
    for i in range(100):
        start_time = time.time()
        response = requests.post(url, json=test_data)
        end_time = time.time()
        
        latency = end_time - start_time
        response_times[test_name].append(latency)
        
        print(f"Request {i + 1} for {test_name}: {latency:.4f} seconds")

with open("multi_test_latency.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Test Case", "Request Number", "Latency (s)"])
    for test_name, latencies in response_times.items():
        for idx, latency in enumerate(latencies):
            writer.writerow([test_name, idx + 1, latency])

df = pd.read_csv("multi_test_latency.csv")

plt.figure(figsize=(10, 6))
df.boxplot(by="Test Case", column="Latency (s)", grid=True)
plt.title("API Latency Boxplot by Test Case")
plt.suptitle("")  
plt.xlabel("Test Case")
plt.ylabel("Latency (seconds)")
plt.tight_layout()
plt.savefig("multi_test_latency_boxplot.png")
plt.show()

average_latencies = df.groupby("Test Case")["Latency (s)"].mean()
print("\nAverage Latency per Test Case:")
print(average_latencies)

