from selenium import webdriver
from selenium.webdriver.common.by import By


from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(100)


with open("datos.txt") as file:
    for i ,line   in enumerate(file):
        usuario=(line)
    sep =","
    dividir =usuario.split(sep)
    try:
        gotdata=dividir[1]
        user=dividir[0]
        pas=dividir[1]
    except: IndexError
gotdata ="null"


print(user)
print(pas)
driver.find_element_by_id("login").send_keys(user)
time.sleep(2)
driver.find_element_by_id("cont").send_keys(pas)
time.sleep(2)
driver.ffind_element_by_id("acceder").send_keys(pas)
time.sleep(2)
driver.ffind_element_by_id("acceder").send_keys(pas)
time.sleep(2)
driver.ffind_element_by_id("acceder").send_keys(pas)
time.sleep(2)
driver.ffind_element_by_id("Erika").send_keys(user)
time.sleep(2)
driver.ffind_element_by_id("Liliana").send_keys(user)
time.sleep(2)
driver.ffind_element_by_id("Espinosa").send_keys(user)
time.sleep(2)
driver.ffind_element_by_id("Senior QA Lead").send_keys(user)
time.sleep(2)
driver.ffind_element_by_id("erikaduque.98@outlook.com").send_keys(user)
time.sleep(2)
driver.ffind_element_by_id("3123360107").send_keys(user)
time.sleep(2)
driver.ffind_element_by_id("file").send_keys(user)
time.sleep(2)
driver.ffind_element_by_id("N/A").send_keys(user)
time.sleep(2)
driver.ffind_element_by_id("2024-27-12").send_keys(user)
time.sleep(2)
driver.ffind_element_by_id("No hay comentarios adicionales").send_keys(user)
time.sleep(2)
driver.ffind_element_by_id("allow").send_keys(pas)
time.sleep(2)
driver.ffind_element_by_id("enviar").send_keys(pas)
time.sleep(2)
file.close()
driver.close()