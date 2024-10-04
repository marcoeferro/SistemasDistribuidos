import requests
import json
from src.scripts.extract.login import login
from src.scripts.extract.data_batery_info_chart import get_data_batery_info_chart
from src.scripts.extract.data_discharging import get_data_discharging
from src.scripts.extract.data_energy_area_chart import get_data_energy_area_chart
from src.scripts.extract.data_energy_bar_chart import get_data_energy_chart
from src.scripts.extract.data_photovoltaic_device import get_data_photovoltaic_device
from src.scripts.extract.data_wheater import get_data_wheater
from src.scripts.extract.data_plant import get_data_plant

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

with open("./data/raw/batery_info.json", "w") as outfile:
    outfile.write(json.dumps(batery_info))

with open("./data/raw/discharging.json", "w") as outfile:
    outfile.write(json.dumps(discharging))

with open("./data/raw/energy_area_chart.json", "w") as outfile:
    outfile.write(json.dumps(energy_area_chart))

with open("./data/raw/energy_bar_chart.json", "w") as outfile:
    outfile.write(json.dumps(energy_bar_chart))

with open("./data/raw/photovoltaic_device.json", "w") as outfile:
    outfile.write(json.dumps(photovoltaic_device))

with open("./data/raw/wheater.json", "w") as outfile:
    outfile.write(json.dumps(wheater))

with open("./data/raw/plant.json", "w") as outfile:
    outfile.write(json.dumps(plant))