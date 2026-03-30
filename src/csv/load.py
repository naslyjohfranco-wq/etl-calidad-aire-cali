import pandas as pd
import mysql.connector

def guardar_datos(df, ruta_salida="Data/processed/datos_limpios.csv"):
    print("Guardando datos transformados...")
    df.to_csv(ruta_salida, index=False)
    print(f"✅ Archivo guardado en: {ruta_salida}")
    



def cargar_csv_mysql(df):

    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="calidad_del_aire_gd"
    )

    cursor = conexion.cursor()

    # 🔽 ESTANDARIZAR
    df.columns = df.columns.str.lower()

    query = """
        INSERT INTO calidad_aire_nacional (fecha, estacion, variable, valor_promedio)
        VALUES (%s, %s, %s, %s)
    """

    # convertir a lista rápida
    datos = list(df[["fecha", "estacion", "variable", "valor_promedio"]].itertuples(index=False, name=None))

    # TAMAÑO DEL BLOQUE
    tamaño_chunk = 5000

    print("⬆️ Insertando datos por bloques...")

    for i in range(0, len(datos), tamaño_chunk):
        chunk = datos[i:i+tamaño_chunk]
        cursor.executemany(query, chunk)
        conexion.commit()
        print(f"Insertadas {i + len(chunk)} filas")

    cursor.close()
    conexion.close()

    print("✅ Carga completada")