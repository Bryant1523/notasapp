# config.py

# Ruta al ejecutable de Tesseract OCR en tu sistema
TESSERACT_CMD_PATH = r'C:\Users\xalbgaray\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

# Ruta a la carpeta que contiene los datos de idioma de Tesseract (ej. spa.traineddata)
TESSDATA_PATH = r"C:\Users\xalbgaray\Desktop\APP_FINAL\tessdata"

# Diccionario de "entrenamiento" para el OCR.
KEYWORDS = {
    'numero_factura': {
        'keywords': ['nota de credito', 'nro. control', 'factura n', 'documento n', 'comprobante n', 'mota crádito'],
        'pattern': r'(\b[0-9-]{5,}\b)'
    },
    'razon_social': {
        'keywords': ['cliente:', 'señor\(es\):', 'razon social del cuente:', 'razon social:', 'a nombre de:', 'nombre:'],
        'pattern': r'([A-ZÁÉÍÓÚÑ\s,.-]+[A-ZÁÉÍÓÚÑ]{2,})'
    },
    'fecha': {
        'keywords': ['fecha:', 'fecha de emision:', 'emitido el:'],
        'pattern': r'(\d{1,2}[/-]\d{1,2}[/-]\d{2,4})'
    },
    'factura_afectada': {
        'keywords': ['factura afectada', 'doc. afectado', 'factura ref', 'documento que modifica'],
        'pattern': r'(\b[0-9-]+\b)'
    }
}

# Alias para las columnas al cargar archivos de datos (Excel/CSV)
COLUMN_ALIASES = {
    'numero_factura': ['factura', 'nro factura', 'documento', 'nro_factura', 'nota de credito'],
    'razon_social': ['cliente', 'razon social', 'nombre', 'razón social', 'señor(es)'],
    'monto_bs': ['monto bs', 'bs', 'bolivares', 'bolívares', 'total'],
    'monto_usd': ['monto usd', 'usd', 'dolares', 'dólares', '$'],
    'fecha': ['fecha emision', 'fecha factura', 'fecha'],
    'portafolio': ['vendedor', 'gestor', 'responsable']
}