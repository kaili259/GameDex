import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DB_PATH = ROOT / "gamedex.db"


def conectar():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def initialize_database():
    conn = conectar()
    cur = conn.cursor()
    
    # Crear tabla si no existe
    cur.execute("""
        CREATE TABLE IF NOT EXISTS videojuegos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            genero TEXT,
            plataforma TEXT,
            anio INTEGER,
            puntuacion REAL,
            caratula TEXT
        )
    """)
    
    # Comprobar si la columna caratula existe, si no, crearla
    cur.execute("PRAGMA table_info(videojuegos)")
    columnas = [col[1] for col in cur.fetchall()]
    if "caratula" not in columnas:
        cur.execute("ALTER TABLE videojuegos ADD COLUMN caratula TEXT")
        
    conn.commit()
    conn.close()


def add_game(titulo, genero, plataforma, anio, puntuacion, caratula=None):
    conn = conectar()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO videojuegos (titulo, genero, plataforma, anio, puntuacion, caratula)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (titulo, genero, plataforma, anio, puntuacion, caratula))
    conn.commit()
    conn.close()


def update_game(id, titulo, genero, plataforma, anio, puntuacion, caratula=None):
    conn = conectar()
    cur = conn.cursor()
    cur.execute("""
        UPDATE videojuegos
        SET titulo=?, genero=?, plataforma=?, anio=?, puntuacion=?, caratula=?
        WHERE id=?
    """, (titulo, genero, plataforma, anio, puntuacion, caratula, id))
    conn.commit()
    conn.close()


def delete_game(id):
    conn = conectar()
    cur = conn.cursor()
    cur.execute("DELETE FROM videojuegos WHERE id=?", (id,))
    conn.commit()
    conn.close()


def get_game(id):
    conn = conectar()
    cur = conn.cursor()
    cur.execute("SELECT * FROM videojuegos WHERE id=?", (id,))
    fila = cur.fetchone()
    conn.close()
    return fila


def get_games(texto="", genero="Todos", plataforma="Todas"):
    conn = conectar()
    cur = conn.cursor()
    sql = "SELECT * FROM videojuegos WHERE 1=1"
    params = []

    if texto:
        sql += " AND (titulo LIKE ? OR genero LIKE ? OR plataforma LIKE ?)"
        like = f"%{texto}%"
        params.extend([like, like, like])

    if genero and genero != "Todos":
        sql += " AND genero = ?"
        params.append(genero)

    if plataforma and plataforma != "Todas":
        sql += " AND plataforma = ?"
        params.append(plataforma)

    sql += " ORDER BY titulo COLLATE NOCASE ASC"
    cur.execute(sql, params)
    filas = cur.fetchall()
    conn.close()
    return filas


def get_filter_values(columna):
    if columna not in ("genero", "plataforma"):
        return []
    conn = conectar()
    cur = conn.cursor()
    cur.execute(f"""
        SELECT DISTINCT {columna} FROM videojuegos
        WHERE {columna} IS NOT NULL AND {columna} != ''
        ORDER BY {columna} COLLATE NOCASE ASC
    """)
    valores = [fila[0] for fila in cur.fetchall()]
    conn.close()
    return valores