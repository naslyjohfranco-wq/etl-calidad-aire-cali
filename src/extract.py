import pandas as pd

def extract_datos():
  print("Extrayendo datos...")
  print("\n Datos de la flora...")
  datos_flora = pd.read_csv("Data/raw/1.-la-flora-2010-2019.csv", encoding="latin-1")
  print(datos_flora.head())
  
  print("\n Datos de la era...")
  datos_era = pd.read_csv("Data/raw/2.-era-2010-2019.csv", encoding="latin-1")
  print(datos_era.head())

  print("\n Datos de la transitoria...")
  datos_transitoria = pd.read_csv("Data/raw/3.-transitoria-2014-2019.csv", encoding="latin-1")
  print(datos_transitoria.head())

  print("\n Datos de la estación de monitoreo pance...")
  datos_pance = pd.read_csv("Data/raw/2013_ene_01_2020_pance.csv", encoding="lati" \
  "n-1")
  print(datos_pance.head())

  print("\n Datos de la estación de monitoreo univalle...")
  datos_univalle = pd.read_csv("Data/raw/2013_ene-01-2021_univalle.csv", encoding="latin-1")
  print(datos_univalle.head())

  print("\n Datos de la estación de monitoreo compartir...")
  datos_compartir = pd.read_csv("Data/raw/2014_ene_01_2020-compartir.csv", encoding="latin-1")
  print(datos_compartir.head())

  print("\nDatos de la estación de monitoreo la ermita...")
  datos_ermita = pd.read_csv("Data/raw/8.-la-ermita-2013-2020.csv", encoding="latin-1")
  print(datos_ermita.head())

  print("\n Datos de la estación de monitoreo canaveralejo...")
  datos_canaveralejo = pd.read_csv("Data/raw/9.-canaveralejo-2013-2020.csv", encoding="latin-1")
  print(datos_canaveralejo.head())

  print("\n Datos de la estación de monitoreo base aérea...")
  datos_base_aerea = pd.read_csv("Data/raw/base-aerea-2013-2019.csv", encoding="latin-1")
  print(datos_base_aerea.head())

  print("\n Datos del formato OA...")
  datos_formato_oa = pd.read_csv("Data/raw/formato-oa-para-el-icaactualizado092020.csv", encoding="latin-1")
  print(datos_formato_oa.head())

  #return datos_flora


extract_datos()