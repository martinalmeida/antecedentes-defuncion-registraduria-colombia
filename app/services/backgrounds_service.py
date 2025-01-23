from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

class BackgroundService:
    def __init__(self):
        self.options = Options()
        self.options.add_argument("start-maximized")
        self.preguntas = {
            "¿ Cuanto es 2 X 3 ?": "6",
            "¿ Cuanto es 3 X 3 ?": "9",
            "¿ Cuanto es 6 + 2 ?": "8",
            "¿ Cuanto es 4 + 3 ?": "7",
            "¿ Cuanto es 5 + 3 ?": "8",
            "¿ Cuanto es 9 - 2 ?": "7",
            "¿ Cuanto es 3 - 2 ?": "1",
            "¿ Cual es la Capital del Vallle del Cauca?": "cali",
            "¿ Cual es la Capital del Atlantico?": "barranquilla",
            "¿ Cual es la Capital de Colombia (sin tilde)?": "bogota",
            "¿ Cual es la Capital de Antioquia (sin tilde)?": "medellin"
        }

    async def search_background(self, payload: dict):
        cedula = payload.get("id_card")
        silent = payload.get("silent", False)
        
        try:
            # Inicializar el navegador
            driver = webdriver.Chrome(service=ChromeService(), options=self.options)
            url = "https://apps.procuraduria.gov.co/webcert/inicio.aspx?tpo=1"
            driver.get(url)
            
            # Minimizar la ventana si silent=True
            if silent:
                driver.minimize_window()
            
            # Completar el formulario
            cedula_input = driver.find_element(By.ID, "txtNumID")
            cedula_input.send_keys(cedula)

            tipo_documento = driver.find_element(By.ID, "ddlTipoID")
            all_options = driver.find_elements(By.TAG_NAME, "option")
            for option in all_options:
                if option.get_attribute("value") == "1":
                    option.click()

            # Resolver la pregunta de seguridad
            pregunta = driver.find_element(By.ID, "lblPregunta").text
            while pregunta not in self.preguntas:
                cambiar_pregunta = driver.find_element(By.ID, "ImageButton1")
                cambiar_pregunta.click()
                time.sleep(1)
                pregunta = driver.find_element(By.ID, "lblPregunta").text

            # Enviar respuesta
            respuesta_input = driver.find_element(By.ID, "txtRespuestaPregunta")
            respuesta_input.send_keys(self.preguntas[pregunta])
            consultar_btn = driver.find_element(By.ID, "btnConsultar")
            consultar_btn.click()

            # Esperar respuesta
            while True:
                if len(driver.find_elements(By.CLASS_NAME, "datosConsultado")) > 0:
                    info = driver.find_element(By.CLASS_NAME, "datosConsultado")
                    raw_html = info.get_attribute("innerHTML")
                    # Usar BeautifulSoup para procesar el HTML
                    soup = BeautifulSoup(raw_html, "html.parser")
                    # Extraer texto y manejar elementos span para nombres
                    spans = soup.find_all('span')
                    nombres = " ".join(span.get_text(strip=True) for span in spans)
                    # Procesar el texto general
                    texto_general = soup.get_text(" ", strip=True)
                    nombre = texto_general.replace("".join(span.get_text(strip=True) for span in spans), nombres)
                    antecedentes = info.find_element(By.XPATH, 'following-sibling::*[1]').get_attribute("innerHTML")
                    break
                time.sleep(1)

            # Cerrar el navegador
            driver.close()

            # Retornar los resultados
            return {
                "name": nombre,
                "info": antecedentes,
                "state": False if antecedentes == "El ciudadano no presenta antecedentes" else True
                }

        except Exception as e:
            # Manejo de errores
            if 'driver' in locals():
                driver.close()
            return str(e)
