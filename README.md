# antecedentes-defuncion-registraduria-colombia

API para consulta de antecedentes penales ante la procuraduria y verificación de personas vivas naturales en Colombia.

## Requisitos

- Python 3.9+
- FastAPI
- Uvicorn

## Instalación

1. Clona el repositorio:

   ```bash
   git clone https://github.com/martinalmeida/core-back-end-api
   ```

2. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

3. Activar el entorno de desarrollo:

   ```bash
   source venv/bin/activate
   ```

4. Inicia el servidor:

   ```bash
   uvicorn app.main:app --reload
   ```

5. (OPCIONAL) Agregar nuevas dependencias al requirements.txt:
   ```bash
   pip freeze > requirements.txt
   ```

6. Hacer petición al API en local por medio de postman al end-point de tipo POST **http://127.0.0.1:8000/test-search-person** y su body:
   ```bash
   {
      "id_card": "99999",
      "ip_address": "192.289.202"
   }
   ```
