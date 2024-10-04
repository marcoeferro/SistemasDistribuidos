import requests
import json
from login import login
from data_batery_info_chart import get_data_batery_info_chart
from data_discharging import get_data_discharging
from data_energy_area_chart import get_data_energy_area_chart
from data_energy_bar_chart import get_data_energy_chart
from data_photovoltaic_device import get_data_photovoltaic_device
from data_wheater import get_data_wheater
from data_plant import get_data_plant

loginUrl = "https://server.growatt.com/login"

session = requests.session()

login(loginUrl,session=session)

batery_info =get_data_batery_info_chart(session=session, loginUrl=loginUrl)
discharging = get_data_discharging(session=session, loginUrl=loginUrl)
energy_area_chart = get_data_energy_area_chart(session=session, loginUrl=loginUrl)
energy_bar_chart = get_data_energy_chart(session=session, loginUrl=loginUrl)
photovoltaic_device = get_data_photovoltaic_device(session=session, loginUrl=loginUrl)
wheater = get_data_wheater(session=session, loginUrl=loginUrl)
plant = get_data_plant(session=session, loginUrl=loginUrl)

# Writing to .json files

with open("./data/batery_info.json", "w") as outfile:
    outfile.write(json.dumps(batery_info))

with open("./data/discharging.json", "w") as outfile:
    outfile.write(json.dumps(discharging))

with open("./data/energy_area_chart.json", "w") as outfile:
    outfile.write(json.dumps(energy_area_chart))

with open("./data/energy_bar_chart.json", "w") as outfile:
    outfile.write(json.dumps(energy_bar_chart))

with open("./data/photovoltaic_device.json", "w") as outfile:
    outfile.write(json.dumps(photovoltaic_device))

with open("./data/wheater.json", "w") as outfile:
    outfile.write(json.dumps(wheater))

with open("./data/plant.json", "w") as outfile:
    outfile.write(json.dumps(plant))