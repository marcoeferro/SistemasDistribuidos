import requests
import json

def get_data_photovoltaic_device(session: requests, loginUrl: str) -> json:
    """
    Args: 
        requests: the login session 
        str(loginUrl): the login url
    Returns:
        json: the api response with the storage energy day chart 
    """
    url = 'https://server.growatt.com/panel/getDevicesByPlantList'

    payload = {
        "currPage":  "1",
        "plantId": "2613959"
    }

    response = session.post(
        url,
        data=payload,
        headers=dict(referer=loginUrl)
    )

    if (response.status_code == 200 ):
        try:
            return json.loads(response.text)
        except ValueError as e:
            print(f"Deserealization - ERROR on photovoltaic device data [ERROR : {e}]")
    else:
        print(f"RESPONSE ERROR on photovoltaic device data request [RESPONSE CODE : {response.status_code}]")