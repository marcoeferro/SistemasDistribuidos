from pathlib import Path
import path_setup # This ensures the sys.path is modified
from utils.json_utils import get_values_by_keys, json_traverser
import json

def transform_plant() -> None:

    # Define the base directory (e.g., the directory of the current script)
    base_dir = Path(__file__).resolve().parent

    # Define the raw data directory relative to the base directory
    raw_data_dir = base_dir/'..'/'..'/'..'/'data'/'raw'

    # Define the path to the raw plant JSON file
    raw_file_path = raw_data_dir / 'plant.json'


    # Define the raw data directory relative to the base directory
    processed_data_dir = base_dir/'..'/'..'/'..'/'data'/'processed'

    # Define the path to the processed plant JSON file
    processed_file_path = processed_data_dir / 'processed_plant.json'

    labels = ["country","formulaCo2","accountName","city","timezone","co2","gridCompany","creatDate","formulaCoal","gridPort","designCompany","fixedPowerPrice","id","lat","valleyPeriodPrice","tempType","lng","locationImg","tree","peakPeriodPrice","installMap","plantType","nominalPower","formulaMoney","formulaTree","flatPeriodPrice","eTotal","protocolId","plantImg","isShare","gridServerUrl","coal","moneyUnit","plantName","moneyUnitText"]

    with raw_file_path.open("r") as file:
        data = json.load(file)
        
        data_raw = json_traverser(data)
        data_cleaned = get_values_by_keys(data=data_raw,keys=labels)

        with processed_file_path.open('w') as outfile:
            json.dump(obj=data_cleaned,fp=outfile)