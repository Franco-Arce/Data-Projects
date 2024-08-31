import sqlite3
import pandas as pd  # Importar pandas aquí

def get_db_connection():
    conn = sqlite3.connect('postulaciones.db', timeout=10)
    return conn

def create_table():
    conn = get_db_connection()
    cursor = conn.cursor()
    # Eliminar la tabla si existe para evitar conflictos
    cursor.execute('DROP TABLE IF EXISTS postulaciones')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS postulaciones (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            estado TEXT NOT NULL,
            fecha TEXT NOT NULL,
            plataforma TEXT,
            empresa TEXT,
            enlace TEXT
        )
    ''')
    conn.commit()
    conn.close()

def add_postulation(titulo, estado, fecha, plataforma, empresa, enlace):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('''
            INSERT INTO postulaciones (titulo, estado, fecha, plataforma, empresa, enlace)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (titulo, estado, fecha, plataforma, empresa, enlace))
        conn.commit()
    finally:
        conn.close()

def delete_postulation(titulo):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('''
            DELETE FROM postulaciones WHERE titulo = ?
        ''', (titulo,))
        conn.commit()
    finally:
        conn.close()

def get_postulations():
    conn = get_db_connection()
    query = 'SELECT * FROM postulaciones'
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

# Asegúrate de crear la tabla al iniciar la aplicación
create_table()
