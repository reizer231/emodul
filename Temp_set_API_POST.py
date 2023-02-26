import requests
import json
import contextlib


url = "https://emodul.eu/api/v1/authentication"
auth_data = {"username": "", "password": ""}
# homeassistant API endpoints
url_outd = "http://192.168.1.X:8123/api/states/sensor.outdoor_temperature"
url_exhaust = "http://192.168.1.X:8123/api/states/sensor.exhaust_temperature"
url_co = "http://192.168.1.X:8123/api/states/sensor.co_temperature"
url_cwu = "http://192.168.1.X:8123/api/states/sensor.cwu_temperature"
headers = {"accordingly to https://emodul.eu/docs/api-v1.txt"}


x = requests.post(url, json=auth_data)
z = x.text
y = json.loads(z)

access_token = y["token"]
my_headers = {"Authorization": "Bearer " + access_token}
url2 = "https://emodul.eu/api/v1/users/{usernumber}/modules/{user_token}"

session = requests.Session()
session.headers.update(my_headers)
response = session.get(url2)
preety_resp = response.text
preety_resp1 = json.loads(preety_resp)

# reaching exact level of indentation to extract value examples below:
temp_outside = (preety_resp1["tiles"][10]["params"]["value"]) / 10
temp_co = (preety_resp1["tiles"][8]["params"]["widget2"]["value"]) / 10
temp_cwu = (preety_resp1["tiles"][9]["params"]["value"]) / 10
temp_exhaust = (preety_resp1["tiles"][11]["params"]["value"]) / 10

# Creating payloads to reach each endpoint

payload_outside = {
    "state": temp_outside,
    "attributes": {
        "state_class": "measurement",
        "unit_of_measurement": "\u00b0C",
        "device_class": "temperature",
        "friendly_name": "Temperatura na zewnątrz",
    },
}
payload_cwu = {
    "state": temp_cwu,
    "attributes": {
        "state_class": "measurement",
        "unit_of_measurement": "\u00b0C",
        "device_class": "temperature",
        "friendly_name": "Temperatura CWU",
    },
}
payload_co = {
    "state": temp_co,
    "attributes": {
        "state_class": "measurement",
        "unit_of_measurement": "\u00b0C",
        "device_class": "temperature",
        "friendly_name": "Temperatura Pieca",
    },
}
payload_exhaust = {
    "state": temp_exhaust,
    "attributes": {
        "state_class": "measurement",
        "unit_of_measurement": "\u00b0C",
        "device_class": "temperature",
        "friendly_name": "Temperatura Spalin",
    },
}

# posting to update instance in home assistant
posting_outside = requests.post(url_outd, headers=headers, json=payload_outside)
posting_exhaust = requests.post(url_exhaust, headers=headers, json=payload_exhaust)
posting_co = requests.post(url_co, headers=headers, json=payload_co)
posting_cwu = requests.post(url_cwu, headers=headers, json=payload_cwu)
