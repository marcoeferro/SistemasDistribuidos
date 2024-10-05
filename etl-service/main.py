import os
from pathlib import Path
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

# Define the base directory (e.g., the directory of the current script)
base_dir = Path(__file__).resolve().parent

# Define the data directory relative to the base directory
data_dir = base_dir / 'data' / 'raw'

# Ensure the directory exists
data_dir.mkdir(parents=True, exist_ok=True)

# Define the path to the batery_info JSON file
file_path = data_dir / 'batery_info.json'


with file_path.open("w") as outfile:
    if(batery_info!=None):
        outfile.write(json.dumps(batery_info))
    else:
        print("ERROR the batery_info data is NULL")
# Define the path to the discharging JSON file
file_path = data_dir / 'discharging.json'

with file_path.open("w") as outfile:
    if(discharging!=None):
        outfile.write(json.dumps(discharging))
    else:
        print("ERROR the discharging data is NULL")
# Define the path to the energy_area_chart JSON file
file_path = data_dir / 'energy_area_chart.json'

with file_path.open("w") as outfile:
    if(energy_area_chart!=None):
        outfile.write(json.dumps(energy_area_chart))
    else:
        print("ERROR the energy_area_chart data is NULL")
# Define the path to the energy_bar_chart JSON file
file_path = data_dir / 'energy_bar_chart.json'

with file_path.open("w") as outfile:
    if(energy_bar_chart!=None):
        outfile.write(json.dumps(energy_bar_chart))
    else:
        print("ERROR the energy_bar_chart data is NULL")
# Define the path to the photovoltaic_device JSON file
file_path = data_dir / 'photovoltaic_device.json'

with file_path.open("w") as outfile:
    if(photovoltaic_device!=None):
        outfile.write(json.dumps(photovoltaic_device))
    else:
        print("ERROR the photovoltaic_device data is NULL")
# Define the path to the wheater JSON file
file_path = data_dir / 'wheater.json'

with file_path.open("w") as outfile:
    if(wheater!=None):
        outfile.write(json.dumps(wheater))
    else:
        print("ERROR the wheater data is NULL")
# Define the path to the plant JSON file
file_path = data_dir / 'plant.json'

with file_path.open("w") as outfile:
    if(plant!=None):
        outfile.write(json.dumps(plant))
    else:
        print("ERROR the plant data is NULL")
