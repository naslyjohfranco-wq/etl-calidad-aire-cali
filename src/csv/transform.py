import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# =========================
# LIMPIEZA BASE
# =========================
def limpiar_base(df):
    df.columns = (
        df.columns
        .str.strip()
        .str.replace('ï»¿', '', regex=False)
        .str.replace('Â', '', regex=False)
    )

    # eliminar columnas basura sin romper otras
    df = df.loc[:, ~df.columns.str.contains("^Unnamed")]

    # reemplazar ND
    df = df.replace("ND", np.nan)

    return df


# =========================
# TRANSFORMACIONES ESPECÍFICAS (SUAVES)
# =========================

def corregir_era(df):
    return df.iloc[1:].copy()


def corregir_univalle(df):
    return df.copy()


def corregir_compartir(df):
    df.columns = df.columns.str.replace('ï»¿', '', regex=False)
    return df.copy()


def corregir_base_aerea(df):
    if "_id" in df.columns:
        df = df.drop(columns=["_id"])
    return df


# =========================
# NORMALIZACIÓN VARIABLES
# =========================
def normalizar_variables(df):
    df["variable"] = (
        df["variable"]
        .str.lower()
        .str.strip()
        .str.replace(" ", "")
        .str.replace("(ug/m3)", "", regex=False)
        .str.replace(".", "", regex=False)
    )

    df["variable"] = df["variable"].replace({
        "pm25": "PM25",
        "pm25ug/m3": "PM25",
        "pm10": "PM10",
        "pm10ug/m3": "PM10",
        "o3": "O3",
        "so2": "SO2",
        "no2": "NO2",
        "co": "CO"
    })

    return df


# =========================
# TRANSFORMACIÓN GENERAL
# =========================
def transformar_df(df, nombre_estacion):

    df = limpiar_base(df)

    if nombre_estacion == "era":
        df = corregir_era(df)
    elif nombre_estacion == "univalle":
        df = corregir_univalle(df)
    elif nombre_estacion == "compartir":
        df = corregir_compartir(df)
    elif nombre_estacion == "base_aerea":
        df = corregir_base_aerea(df)

    # detectar fecha
    columnas_fecha = [c for c in df.columns if "fecha" in c.lower()]

    if len(columnas_fecha) == 0:
        raise ValueError(f"No hay columna de fecha en {nombre_estacion}")

    col_fecha = columnas_fecha[0]

    # convertir fecha
    df[col_fecha] = pd.to_datetime(df[col_fecha], errors="coerce")

    # convertir numéricos
    for col in df.columns:
        if col != col_fecha:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    df = df.rename(columns={col_fecha: "datetime"})
    df["estacion"] = nombre_estacion.upper()

    # columnas para melt
    columnas_id = ["datetime", "estacion"]
    columnas_valor = [c for c in df.columns if c not in columnas_id]

    if len(columnas_valor) == 0:
        print(f"⚠️ {nombre_estacion} sin variables")
        return pd.DataFrame()

    df = df.melt(
        id_vars=columnas_id,
        value_vars=columnas_valor,
        var_name="variable",
        value_name="valor"
    )

    return df


# =========================
# PROMEDIO DIARIO
# =========================
def agregar_promedio_diario(df):

    df["fecha"] = df["datetime"].dt.date

    df_diario = (
        df.groupby(["fecha", "estacion", "variable"])["valor"]
        .mean()
        .reset_index()
    )

    df_diario = df_diario.rename(columns={"valor": "valor_promedio"})

    return df_diario


# =========================
# TRANSFORMAR TODOS
# =========================
def transformar_todos(diccionario_datos):

    lista_df = []

    for nombre, df in diccionario_datos.items():
        try:
            print(f"🔧 Transformando {nombre}")
            df_t = transformar_df(df, nombre)
            lista_df.append(df_t)
        except Exception as e:
            print(f"❌ Error en {nombre}: {e}")

    df_final = pd.concat(lista_df, ignore_index=True)

    # limpieza
    df_final = df_final.dropna(subset=["datetime", "valor"])

    # normalizar variables
    df_final = normalizar_variables(df_final)

    # 🔥 solo contaminantes
    contaminantes = ["PM10", "PM25", "O3", "SO2", "NO2", "CO"]
    df_final = df_final[df_final["variable"].isin(contaminantes)]

    # ordenar
    df_final = df_final.sort_values("datetime")

    # 🔥 promedio diario
    df_diario = agregar_promedio_diario(df_final)

    return df_final, df_diario