import requests
import json

def get_data_batery_info_chart(session: requests, loginUrl: str) -> json:
    """
    Args: 
        requests: the login session 
        str(loginUrl): the login url
    Returns:
        json: the api response with the storage energy day chart 
    """
    url = 'https://server.growatt.com/panel/storage/getStorageBatChart'

    payload = {
        "date": "2024-10-02",
        "plantId": "2613959",
        "storageSn": "JNK1CHE00V"
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
            print(f"Deserealization - ERROR on batery info chart data [ERROR : {e}]")
    else:
        print(f"RESPONSE ERROR on batery info chart data request [RESPONSE CODE : {response.status_code}]")