from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from colorama import init, Fore, Style
from bs4 import BeautifulSoup as b
import time, sys, re, os, pyfiglet

login_array=[]
init(autoreset=True)
GREEN=f"{Fore.GREEN}{Style.BRIGHT}"
WHITE=f"{Fore.WHITE}{Style.BRIGHT}"

def login(user, password):
 chromedriver_path = "./driver/chromedriver"
 options = Options()
 options.add_argument("--disable-gpu")
 options.add_argument("--headless=new")
 service = Service(executable_path=chromedriver_path)
 driver = webdriver.Chrome(service=service, options=options)
 wait = WebDriverWait(driver, 60)
 driver.set_page_load_timeout(300)
 linkBDV='https://bdvenlinea.banvenez.com/'
 try:
  print(f"{GREEN}[+]{WHITE} Cargando página del BDV...")
  driver.get(linkBDV)
 except:
  print("Ocurrio un error")
  driver.quit()
  sys.exit()
 print(f"{GREEN}[+]{WHITE} Estas en el BDV [AHORA]\n{GREEN}[+]{WHITE} Introduciendo Usuario")
 user_field = wait.until(EC.presence_of_element_located((By.ID, "mat-input-0")))
 user_field.send_keys(user + Keys.RETURN)
 print(f"{GREEN}[+]{WHITE} Introduciendo contraseña...")
 pass_field = wait.until(EC.presence_of_element_located((By.ID, "mat-input-1")))
 pass_field.send_keys(password)
 login_array.append(0)
 continuar_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='mat-button-wrapper' and contains(text(), 'Continuar')]")))
 continuar_btn.click()
 print(f"{GREEN}[+]{WHITE} Logueandome")
 return driver

def save(page):
 with open('website.html', 'w') as f:
  f.write(page)
  f.close()

def show():
 with open('website.html', 'r') as f:
  read=f.read()
  soup=b(read, 'html.parser')
  find=soup.find_all('td', class_="cells-container-center-petro saldo")
  money=f"{GREEN}[+]{WHITE} Saldo Disponible : {GREEN}{find[1].text.strip()}\n"
  print(money)
  os.remove("website.html")
  sys.exit()

def showMoney(driver):
 print(f"{GREEN}[+]{WHITE} Te logueastes con exito")
 time.sleep(5)
 if login_array[0] == 0:
  visibility_icons = driver.find_elements(By.XPATH, "//mat-icon[contains(@class, 'material-icons') and contains(text(), 'visibility')]")
  if visibility_icons:
   visibility_icons[0].click()
   time.sleep(4)
  else:
   print("No se encontro el icono de visibilidad")
  page=driver.page_source
  save(page)
  show()

if __name__ == '__main__':
 try:
  os.system("clear")
  #ansi_shadow
  print(f"\n{GREEN}" + pyfiglet.figlet_format("BDVscript", font="ansi_shadow") + f"{WHITE}")
  user=input(f"{GREEN}[+]{WHITE} Introduce tu usuario : {GREEN}")
  password=input(f"{GREEN}[+]{WHITE} Introduce tu contraseña: {GREEN}")
  print("")
  driver=login(user, password)
  if driver:
   showMoney(driver)
  input()
 except KeyboardInterrupt:
  print("Finalizo el script")
