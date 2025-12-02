import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
from datetime import datetime

SCOPE = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]
CREDS_FILE = "credentials.json"
SPREADSHEET_NAME = "Mi Base de Datos de Creditos" 

@st.cache_resource
def connect_to_sheet():
    try:
        creds = ServiceAccountCredentials.from_json_keyfile_name(CREDS_FILE, SCOPE)
        client = gspread.authorize(creds)
        return client
    except Exception as e:
        st.error(f"Error de conexión con Google Sheets: {e}")
        st.info("Asegúrate de que el archivo 'credentials.json' esté en la misma carpeta y sea correcto.")
        return None

@st.cache_data(ttl=300)
def get_all_data(_client):
    try:
        spreadsheet = _client.open(SPREADSHEET_NAME)
        worksheet = spreadsheet.get_worksheet(0)
        all_data = worksheet.get_all_records()
        if not all_data:
            return pd.DataFrame()
        return pd.DataFrame(all_data)
    except gspread.exceptions.SpreadsheetNotFound:
        st.error(f"No se encontró la Hoja de Cálculo llamada '{SPREADSHEET_NAME}'. Verifica el nombre y que esté compartida.")
        return pd.DataFrame()
    except Exception as e:
        st.error(f"Error al leer los datos de Google Sheet: {e}")
        return pd.DataFrame()

def guardar_en_sheet(df: pd.DataFrame, filename: str):
    client = connect_to_sheet()
    if not client or df is None or df.empty:
        return

    try:
        spreadsheet = client.open(SPREADSHEET_NAME)
        worksheet = spreadsheet.get_worksheet(0)
        
        df_to_save = df.copy()
        df_to_save['archivo_origen'] = filename
        df_to_save['fecha_procesado'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        header = worksheet.row_values(1) if worksheet.row_count > 0 else []

        if not header:
            worksheet.update([df_to_save.columns.values.tolist()], 'A1')

        data_to_append = df_to_save.values.tolist()
        if data_to_append:
            worksheet.append_rows(data_to_append, value_input_option='USER_ENTERED')
            st.cache_data.clear()
    except Exception as e:
        st.error(f"Error al guardar en Google Sheet: {e}")

def buscar_por_palabra_clave(df: pd.DataFrame, keyword: str) -> pd.DataFrame:
    if df.empty or not keyword:
        return pd.DataFrame()
    
    try:
        mask = (df['razon_social'].astype(str).str.contains(keyword, case=False, na=False) |
                df['numero_factura'].astype(str).str.contains(keyword, case=False, na=False) |
                df['portafolio'].astype(str).str.contains(keyword, case=False, na=False) |
                df['archivo_origen'].astype(str).str.contains(keyword, case=False, na=False))
        return df[mask]
    except Exception as e:
        st.error(f"Error durante la búsqueda: {e}")
        return pd.DataFrame()