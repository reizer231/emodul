import requests
import json
import contextlib
 

url = 'https://emodul.eu/api/v1/authentication'
auth_data = {"username":"your_usr", "password":"your_pass"}

x = requests.post(url, json = auth_data)
z = x.text
y = json.loads(z)
access_token = y["token"]
my_headers = {'Authorization':'Bearer '+access_token}
url2 = 'https://emodul.eu/api/v1/users/your_usr_numb/modules/your_user'

session = requests.Session()
session.headers.update(my_headers)
response = session.get(url2)
preety_resp = response.text
preety_resp1 = json.loads(preety_resp)


temp_outside = (preety_resp1['tiles'][10]['params']['value'])/10
temp_co = (preety_resp1['tiles'][8]['params']['widget2']['value'])/10
temp_cwu = (preety_resp1['tiles'][9]['params']['value'])/10
temp_exhaust = (preety_resp1['tiles'][11]['params']['value'])/10
print(temp_outside, temp_cwu, temp_co, temp_exhaust)
