from pathlib import Path
from src.utils.json_utils import json_traverser, get_values_by_keys
import json

# Define the base directory (e.g., the directory of the current script)
base_dir = Path(__file__).resolve().parent

# Define the raw data directory relative to the base directory
raw_data_dir = base_dir/'..'/'..'/'..'/'data'/'raw'

# Define the path to the raw discharging JSON file
raw_file_path = raw_data_dir / 'discharging.json'


# Define the raw data directory relative to the base directory
processed_data_dir = base_dir/'..'/'..'/'..'/'data'/'processed'

# Define the path to the processed discharging JSON file
processed_file_path = processed_data_dir / 'processed_discharging.json'

tags = ["deviceType","useEnergyToday","chargeToday","eDischargeTotal","eDischargeToday","useEnergyTotal","eToUserTotal","epvToday","epvTotal","chargeTotal","eToGridToday","eToUserToday","eToGridTotal"]

with raw_file_path.open("r") as file:
    data = json.load(file)
    
    data_raw = json_traverser(data)
    data_cleaned = get_values_by_keys(data=data_raw,keys=tags)

    with processed_file_path.open('w') as outfile:
        json.dump(obj=data_cleaned,fp=outfile)
