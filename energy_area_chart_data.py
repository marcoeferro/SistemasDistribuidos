import requests
import json

#sesion
sesion = requests.session()

#detalles del login
payload = {
    "account":"absch",
    "password":"Unvime24",
    "validateCode":""
}

loginUrl = "https://server.growatt.com/login"

result = sesion.post(
    loginUrl,
    data = payload,
    headers = dict(referer=loginUrl)
)

url = 'https://server.growatt.com/panel/storage/getStorageEnergyDayChart'

payload = {
            "date": "2024-10-02",
            "plantId": "2613959",
            "storageSn": "JNK1CHE00V"
}

result = sesion.post(
    url,
    data=payload,
    headers=dict(referer=loginUrl)
)

growattData = json.loads(result.text) 
print(growattData)