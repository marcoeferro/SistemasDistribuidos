from playwright.sync_api import sync_playwright
import json

def login_and_get_data():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        
        # Login
        login_url = "https://server.growatt.com/login"
        page.goto(login_url)
        page.get_by_placeholder("Nombre de usuario").fill("absch")
        page.get_by_placeholder("Contraseña").fill("Unvime24")
        page.get_by_role("button", name="Registrarse").click()
        
        # Wait for login to complete
        page.wait_for_selector("svg.highcharts-root ")
        
        # Get cookies after login
        cookies = context.cookies()
        
        # Prepare headers and payload for the request
        headers = {
            "accept": "application/json, text/javascript, */*; q=0.01",
            "accept-language": "es-419,es;q=0.9,es-ES;q=0.8,en;q=0.7,en-GB;q=0.6,en-US;q=0.5,es-MX;q=0.4",
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "sec-ch-ua": "\"Microsoft Edge\";v=\"129\", \"Not=A?Brand\";v=\"8\", \"Chromium\";v=\"129\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "x-requested-with": "XMLHttpRequest",
            "referer": login_url
        }
        
        payload = {
            "date": "2024-10-02",
            "plantId": "2613959",
            "storageSn": "JNK1CHE00V"
        }
        
        # Send the request using the same session
        response = page.request.post(
            "https://server.growatt.com/panel/storage/getStorageEnergyDayChart",
            headers=headers,
            data=payload
        )
        
        try:
            growatt_data = response.json()
            print(growatt_data)
        except ValueError:
            print("La respuesta no es un JSON válido o está vacía.")
            print(response.text())
        
        context.close()
        browser.close()

if __name__ == "__main__":
    login_and_get_data()
