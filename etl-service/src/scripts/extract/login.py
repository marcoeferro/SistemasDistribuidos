import requests

def login(loginUrl:str,session:requests) -> requests:
    """
    Args: 
        str: the login url
    Returns:
        requests: the api response to the login  
    """

    #detalles del login
    payload = {
        "account":"absch",
        "password":"Unvime24",
        "validateCode":""
    }

    response = session.post(
        loginUrl,
        data=payload,
        headers=dict(referer=loginUrl)
    )

    if (response.status_code == 200 ):
        try:
            return response
        except ValueError as e:
            print(f"Deserealization - ERROR on login data [ERROR : {e}]")
    else:
        print(f"RESPONSE ERROR on login data request [RESPONSE CODE : {response.status_code}]")
