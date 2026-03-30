import pandas as pd
import mysql.connector

def guardar_datos(df, ruta_salida="Data/processed/datos_limpios.csv"):
    print("Guardando datos transformados...")
    df.to_csv(ruta_salida, index=False)
    print(f"✅ Archivo guardado en: {ruta_salida}")
    



def cargar_csv_mysql(df):

    #print("📥 Leyendo CSV...")
    #df = pd.read_csv(ruta_csv)
    

    print("🔌 Conectando a MySQL...")

    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="calidad_del_aire_gd"
    )

    cursor = conexion.cursor()

    # =========================
    # CREAR TABLA (si no existe)
    # =========================
    print("🛠️ Creando tabla si no existe...")

    cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS calidad_aire_nacional (
            DATETIME DATETIME,
            ESTACION VARCHAR(100),
            VARIABLE VARCHAR(100),
            VALOR DECIMAL(65, 0)
        )
    """)

    # =========================
    # INSERTAR DATOS
    # =========================
    print("⬆️ Insertando datos...")

    query = f"""
        INSERT INTO calidad_aire_nacional (DATETIME, ESTACION, VARIABLE, VALOR)
        VALUES (%s, %s, %s, %s)
    """

    datos = []

    for _, fila in df.iterrows():
        datos.append((
            fila["DATETIME"],
            fila["ESTACION"],
            fila["VARIABLE"],
            fila["VALOR"]
        ))

    cursor.executemany(query, datos)

    conexion.commit()

    print(f"{cursor.rowcount} filas insertadas")

    cursor.close()
    conexion.close()

    print("🔒 Conexión cerrada")