import pandas as pd
import matplotlib.pyplot as plt


def analizar_datos(df):
    # Histograma de variables
    plt.figure(figsize=(10, 6))
    plt.hist(df["variable"], bins=20, color='blue', edgecolor='black')
    plt.xlabel("Variables")
    plt.ylabel("Cantidad de datos")
    plt.title("Numero de datos por variable")
    plt.grid(True)
    plt.savefig("Data/processed/histograma_variables.png")


    plt.figure(figsize=(10, 6))
    plt.hist(df["estacion"], bins=20, color='#39A0A3', edgecolor='black')
    plt.xlabel("Estaciones")
    plt.ylabel("Cantidad de datos")
    plt.title("Numero de datos por estación")   
    plt.grid(True)
    plt.tight_layout()

    plt.savefig("Data/processed/histograma_estaciones.png")