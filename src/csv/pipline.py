from .extract import extraer_datos
from .transform import transformar_todos
from .load import cargar_csv_mysql, guardar_datos
from src.api.extract_api import main_api
from .analisis import analizar_datos

def main():
    # 1. Extraer
    datos = extraer_datos()

    # 2. Transformar
    df_horario, df_diario = transformar_todos(datos)

    # 🔍 Verificar datos
    print("\nDatos horarios:")
    print(df_horario.head())

    print("\n Datos diarios:")
    print(df_diario.head())
    
    print(df_diario.describe())

    # 3. Cargar (guardar)
    guardar_datos(df_horario, "Data/processed/datos_horarios.csv")
    guardar_datos(df_diario, "Data/processed/datos_diarios.csv")
    
    cargar_csv_mysql(df_diario)
    
    main_api()
    
    analizar_datos(df_diario)
    


if __name__ == "__main__":
    main()