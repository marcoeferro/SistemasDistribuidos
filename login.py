import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://server.growatt.com/error.do?errorMess=errorNoLogin")
    page.goto("https://server.growatt.com/login")
    page.get_by_placeholder("Nombre de usuario").click()
    page.get_by_placeholder("Nombre de usuario").fill("absch")
    page.get_by_placeholder("Contraseña").click()
    page.get_by_placeholder("Contraseña").fill("Unvime24")
    page.get_by_role("button", name="Registrarse").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
