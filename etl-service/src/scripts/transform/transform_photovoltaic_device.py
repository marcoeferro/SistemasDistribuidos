from pathlib import Path
import path_setup # This ensures the sys.path is modified
from utils.json_utils import get_values_by_keys, json_traverser
import json

def transform_photovoltaic_device() -> None:

    # Define the base directory (e.g., the directory of the current script)
    base_dir = Path(__file__).resolve().parent

    # Define the raw data directory relative to the base directory
    raw_data_dir = base_dir/'..'/'..'/'..'/'data'/'raw'

    # Define the path to the raw photovoltaic_device JSON file
    raw_file_path = raw_data_dir / 'photovoltaic_device.json'


    # Define the raw data directory relative to the base directory
    processed_data_dir = base_dir/'..'/'..'/'..'/'data'/'processed'

    # Define the path to the processed photovoltaic_device JSON file
    processed_file_path = processed_data_dir / 'processed_photovoltaic_device.json'


    labels = ["deviceType","ptoStatus","timeServer","accountName","timezone","plantId","deviceTypeName","nominalPower","bdcStatus","eToday","eMonth","datalogTypeTest","eTotal","pac","datalogSn","alias","location","deviceModel","sn","plantName","status","lastUpdateTime"]
    with raw_file_path.open("r") as file:
        data = json.load(file)
        
        data_raw = json_traverser(data)
        
        data_raw.update(json_traverser(dict(data_raw["datas"][0])))
        
        print(f"LEAFS NODES {data_raw}")
        data_cleaned = get_values_by_keys(data=data_raw,keys=labels)

        with processed_file_path.open('w') as outfile:
            json.dump(obj=data_cleaned,fp=outfile)