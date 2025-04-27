import os
import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
from time import sleep


MARKETPLACE = ["FALABELLA-TODODESCUENTO", "MercadoLibre TodoDescuento", "PARIS-TODODESCUENTO", "Ripley - TODODESCUENTO"]

load_dotenv(dotenv_path='./some_data.env')

CHROME_DRIVER_PATH = os.getenv("CHROME")
BRAVE_DRIVER_PATH = os.getenv("BRAVE")
USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")

#Obtaines the connection to the web page
def connect(URL):
    options = Options()
    options.add_argument("--disable-usb-discovery")
    options.add_argument("--disable-features=WebUSB")
    options.binary_location = BRAVE_DRIVER_PATH

    service = Service(CHROME_DRIVER_PATH)
    driver = webdriver.Chrome(service=service, options=options)

    driver.get(URL)
    return driver


def wait_for_element(connection, element, duration):
    wait = WebDriverWait(connection, duration)
    element_found = wait.until(EC.presence_of_element_located(element))
    return element_found

#Autocomplete authentication and wait for captcha to be ready
def login(connection):
    #Add script for catch verification in a new brand
    sleep(2)
    connection.find_element(By.NAME, "email").send_keys(USER)#ACCESS DATA
    connection.find_element(By.ID, "password").send_keys(PASSWORD)#ACCESS DATA

#Click on the error sync button
def error_sync_button(connection, marketplace):
    cont = 0
    while cont < 3:
        table = wait_for_element(connection, (By.ID, ('DataTables_Table_' + str(cont))), 3)
        row = table.find_element(By.XPATH, '//tr[./td[contains(., "' + marketplace + '")]]')
        row.find_element(By.CSS_SELECTOR, '[uib-popover="Ver productos con error de sincronización"]').click()
        cont = 3
        sleep(5)
    else:
        cont += 1
    products_error()

def products_error():
    pass

def main():
    URL = 'https://app.multivende.com/login'
    connection = connect(URL)
    login(connection)
    sleep(10)
    error_sync_button(connection, "MercadoLibre TodoDescuento")

if __name__ == '__main__':
    main()