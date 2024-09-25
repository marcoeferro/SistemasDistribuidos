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

url = 'https://server.growatt.com/panel/getDevicesByPlantList' 

payload = {
        "currPage":  "1",
        "plantId": "2613959"
}

result = sesion.post(
    url,
    data=payload,
    headers=dict(referer=loginUrl)
)


growattData         = json.loads(result.text)   #pasamos a un json
growattDataObj      = growattData["obj"]        #dejamos la seccion obj
growattDataObjDatas = growattDataObj['datas']   #dejamos la seccion datas

deviceModel = growattDataObjDatas[0]['deviceModel']
growattCurrentPAC            = growattDataObjDatas[0]['pac']                # Current power
growattCurrentNominal_power  = growattDataObjDatas[0]['nominalPower']      # Maximum power
growattCurrentlastUpdateTime = growattDataObjDatas[0]['lastUpdateTime']     # Last Updated

#Show data

print(f"Modelo : {deviceModel}")
print(f"potencia actual : {growattCurrentPAC}")
print(f"potencia maxima : {growattCurrentNominal_power}")
print(f"ultima actualizacion :{growattCurrentlastUpdateTime}")
print(growattData)

"""

# Energy bar chart 
https://server.growatt.com/panel/storage/getStorageEnergyDayChart

# Energy area chart 
https://server.growatt.com/panel/storage/getStorageStatusData?plantId=2613959

# batery info  chart 
https://server.growatt.com/panel/storage/getStorageBatChart

# Wheather Data
https://server.growatt.com/index/getWeatherByPlantId?plantId=2613959

# Photovoltaic Device Data
https://server.growatt.com/panel/getDevicesByPlantList

# Discarging 
https://server.growatt.com/panel/storage/getStorageTotalData?plantId=2613959


"""

