from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

# Configurar las opciones de Chrome
chrome_options = Options()
chrome_options.add_argument("--start-maximized")

# Crear una nueva instancia del navegador Chrome usando WebDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Navegar a la página web
driver.get('https://uttorreon.mx/')

# Esperar a que se cargue la página
driver.implicitly_wait(10)

# Encontrar el campo de usuario/email y la contraseña, luego ingresar las credenciales
usuario_field = driver.find_element(By.ID, "email")
usuario_field.send_keys("20170015")

password_field = driver.find_element(By.ID, "password")
password_field.send_keys("jhon8715608")

# Encontrar y hacer clic en el botón de inicio de sesión
login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
login_button.click()

# Esperar unos segundos para asegurarse de que la página se ha cargado
time.sleep(5)

# Navegar a "Mi Espacio"
mi_espacio_link = driver.find_element(By.LINK_TEXT, "Mi Espacio")
mi_espacio_link.click()

# Esperar unos segundos para asegurarse de que la página se ha cargado
time.sleep(2)

# Navegar a "Académico"
academico_link = driver.find_element(By.XPATH, "//span[text()='Académico']")
academico_link.click()

# Esperar unos segundos para asegurarse de que la página se ha cargado
time.sleep(2)

# Navegar a "Mis Calificaciones"
calificaciones_link = driver.find_element(By.XPATH, "//span[text()='Mis Calificaciones']")
calificaciones_link.click()

# Esperar unos segundos para asegurarse de que la página se ha cargado
time.sleep(2)

# Hacer clic en el enlace "Histórico de calificaciones"
historico_calificaciones_link = driver.find_element(By.ID, "OConsultarCalificaciones")
historico_calificaciones_link.click()

# Esperar unos segundos para asegurarse de que la página se ha cargado
time.sleep(5)

# Hacer scroll hasta el final de la página
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# Esperar unos segundos para ver el resultado (opcional)
time.sleep(5)

# Cambiar la cantidad de registros mostrados a 100
#dropdown_button = driver.find_element(By.XPATH, "//button[@data-toggle='dropdown']")
#dropdown_button.click()

# Esperar un momento para que el dropdown se muestre
#time.sleep(1)

# Seleccionar la opción de 100 registros por página
#option_100 = driver.find_element(By.XPATH, "//a[text()='100']")
#option_100.click()

# Esperar unos segundos para que se recarguen los datos (opcional)
#time.sleep(5)

# Extraer los datos de la tabla
# Nota: Ajusta el selector según la estructura real de la tabla en la página
table_rows = driver.find_elements(By.XPATH, "//table/tbody/tr")

# Inicializar una lista para almacenar los datos
data = []

# Recorrer las filas de la tabla y extraer los datos
for row in table_rows:
    cols = row.find_elements(By.TAG_NAME, "td")
    # Filtrar filas vacías y asegurarse de que hay celdas con texto
    if cols:
        col_texts = [col.text.strip() for col in cols]
        if all(col_texts):  # Solo agregar filas que no estén vacías
            data.append(col_texts)

# Crear un DataFrame de pandas con los datos extraídos
df = pd.DataFrame(data, columns=["Periodo", "Profesor", "Materia", "Unidades", "Final"])

# Guardar el DataFrame en un archivo Excel
df.to_excel("calificaciones.xlsx", index=False)

# Cerrar el navegador
driver.quit()
