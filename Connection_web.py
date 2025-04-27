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

load_dotenv()

#Obtaines the connection to the web page
def connect(URL, BRAVE_PATH):
    options = Options()
    options.binary_location = BRAVE_PATH

    service = Service()#CHROME_DRIVER_PATH
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
    connection.find_element(By.NAME, "email").send_keys("")#DATOS DE ACCESO
    connection.find_element(By.ID, "password").send_keys("")#DATOS DE ACCESO
    
    #Switch to the captcha iframe
    '''iframe = wait_for_element(connection, (By.TAG_NAME, "iframe"), 10)
    connection.switch_to.frame(iframe)
    checkbox = wait_for_element(connection, (By.ID, "recaptcha-anchor"), 10)
    catcha_status = checkbox.get_attribute("aria-checked") 
    print(catcha_status)
    if catcha_status == "true":
        connection.find_element(By.CLASS_NAME, "btn btn-account-submit b-0 br-2 mr-5 ng-binding").click()'''

#Click on the error sync button
def error_sync_button(connection, marketplace):
    cont = 0
    while cont < 3:
        table = wait_for_element(connection, (By.ID, ('DataTables_Table_' + str(cont))), 5)
        row = table.find_element(By.XPATH, '//tr[./td[contains(., "' + marketplace + '")]]')
        row.find_element(By.CSS_SELECTOR, '[uib-popover="Ver productos con error de sincronización"]').click()
        sleep(15)
    else:
        print("Buscando tabla...")
        cont += 1


def main():
    URL = 'https://app.multivende.com/login'
    BRAVE_PATH = #BRAVE_DRIVER_PATH
    connection = connect(URL, BRAVE_PATH)
    login(connection)
    sleep(10)
    error_sync_button(connection, "MercadoLibre TodoDescuento")

if __name__ == '__main__':
    main()