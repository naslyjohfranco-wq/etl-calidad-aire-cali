import requests
import pandas as pd


def extraer_api(resource_id, limite=1000):
    url = "https://datos.cali.gov.co/api/3/action/datastore_search"

    offset = 0
    datos_totales = []

    while True:
        params = {
            "resource_id": resource_id,
            "limit": limite,
            "offset": offset
        }

        response = requests.get(url, params=params)
        data = response.json()

        registros = data["result"]["records"]

        if not registros:
            break

        datos_totales.extend(registros)
        offset += limite

    return pd.DataFrame(datos_totales)


def main_api():
    print("🌐 Extrayendo datos desde API de Cali...")

    resource_id = "b247bee0-596c-4515-bdd4-2ebdf6542caf"

    df = extraer_api(resource_id)

    print("\n Datos obtenidos:")
    print(df.head())

    # Guardar CSV
    ruta = "Data/processed/datos_api_cali.csv"
    df.to_csv(ruta, index=False)

    print(f"\n Datos guardados en: {ruta}")
