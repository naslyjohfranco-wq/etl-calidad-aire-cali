import pandas as pd

def extract_datos():
  datos_flora = pd.read_csv("Data/raw/1.-la-flora-2010-2019.csv", encoding="latin-1")
  print(datos_flora.head())

  data_frame = pd.DataFrame(datos_flora)
  print(data_frame.head())

  #return datos_flora


extract_datos()