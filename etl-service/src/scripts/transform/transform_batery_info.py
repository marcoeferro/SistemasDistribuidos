from pathlib import Path
import path_setup # This ensures the sys.path is modified
from utils.json_utils import get_values_by_keys, json_traverser
import json

def transform_batery_info() -> None:

    # Define the base directory (e.g., the directory of the current script)
    base_dir = Path(__file__).resolve().parent

    # Define the raw data directory relative to the base directory
    raw_data_dir = base_dir/'..'/'..'/'..'/'data'/'raw'

    # Define the path to the raw batery_info JSON file
    raw_file_path = raw_data_dir / 'batery_info.json'


    # Define the raw data directory relative to the base directory
    processed_data_dir = base_dir/'..'/'..'/'..'/'data'/'processed'

    # Define the path to the processed batery_info JSON file
    processed_file_path = processed_data_dir / 'processed_batery_info.json'

    labels = ['date','cdsTitle','capacity','cd_charge','cd_disCharge']

    with raw_file_path.open("r") as file:
        data = json.load(file)
        
        data_raw = json_traverser(data)
        data_cleaned = get_values_by_keys(data=data_raw,keys=labels)

        with processed_file_path.open('w') as outfile:
            json.dump(obj=data_cleaned,fp=outfile)