import requests
import json

url = "http://ece444practical5-env.eba-5cgzpauf.us-east-2.elasticbeanstalk.com/predict"

fake_test_1 = {
    "text": "Share a certain post of Bill Gates on Facebook and he will send you money."  
}

fake_test_2 = {
    "text": "A Fargo, North Dakota, man was arrested for clearing snow with a flamethrower."  
}

real_test_1 = {
    "text": "Business groups, opposition parties and the Ontario government react to Trudeau government’s major cut in permanent resident targets." 
}

real_test_2 = {
    "text": "More than 20 lawmakers from his party sign letter asking Canadian prime minister to step down before election"  
}

response = requests.post(url, json=fake_test_1)

if response.status_code == 200:
    result = response.json()
    print(f"Prediction: {result['prediction']}")
else:
    print(f"Error: {response.status_code} - {response.text}")

response2 = requests.post(url, json=fake_test_2)

if response2.status_code == 200:
    result = response2.json()
    print(f"Prediction: {result['prediction']}")
else:
    print(f"Error: {response2.status_code} - {response2.text}")

response3 = requests.post(url, json=real_test_1)

if response3.status_code == 200:
    result = response3.json()
    print(f"Prediction: {result['prediction']}")
else:
    print(f"Error: {response3.status_code} - {response3.text}")

response4 = requests.post(url, json=real_test_2)

if response4.status_code == 200:
    result = response4.json()
    print(f"Prediction: {result['prediction']}")
else:
    print(f"Error: {response4.status_code} - {response4.text}")
