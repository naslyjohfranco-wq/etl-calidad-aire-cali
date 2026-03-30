import pandas as pd


def extraer_datos():
    print("🔄 Extrayendo datos...\n")

    rutas_archivos = {
        "La Flora": "Data/raw/1.-la-flora-2010-2019.csv",
        "Era": "Data/raw/2.-era-2010-2019.csv",
        "Transitoria": "Data/raw/3.-transitoria-2014-2019.csv",
        "Pance": "Data/raw/2013_ene_01_2020_pance.csv",
        "Univalle": "Data/raw/2013_ene-01-2021_univalle.csv",
        "compartir": "Data/raw/2014_ene_01_2020-compartir.csv",
        "la Ermita": "Data/raw/8.-la-ermita-2013-2020.csv",
        "Canaveralejo": "Data/raw/9.-canaveralejo-2013-2020.csv",
        "Base Aerea": "Data/raw/base-aerea-2013-2019.csv"
    }

    dataframes = {}

    for nombre, ruta in rutas_archivos.items():
        try:
            print(f"Leyendo datos de: {nombre}...")

            df = pd.read_csv(ruta, encoding="latin-1")

            print(df.head(), "\n")

            dataframes[nombre] = df
            

        except Exception as e:
            print(f"❌ Error leyendo {nombre}: {e}")

    print("✅ Extracción finalizada\n")

    return dataframes
