from fastapi import FastAPI
from typing import List
from pydantic import BaseModel
import sqlite3
import statistics
app = FastAPI


"""
Modelos
"""
class Calificacion(BaseModel):
    materia: str
    nota: float

class Estudiante(BaseModel):
    nombre: str
    calificacion:List[Calificacion]

"""
Base de datos simulada
"""
def get_db():
    conn = sqlite3.connect("escuela.bd")
    return conn

def crear_tabla():
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXIST estudiantes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT
                   
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXIST calificaciones (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        estudiante_id INTEGER,
        materia TEXT,
        nota REAL,
        FOREIGN KEY (estudiante_id) REFERENCES estudiantes (id)
    )
    """)
    

"""
Funcion IA Simple
"""

def evaluar_desempeno(notas):
    promedio = statistics.mean(notas)

    if promedio >= 9:
        estado = "Excelente"
        recomendacion = "Puedes participar en proyecto"
    
    elif promedio >= 7:
        estado = "Regular"
        recomendacion = "Necesitas reforzar algunos temas"

    else:
        estado = "En riesgo"
        recomendacion = "Requiere tutotias urgentes"
    
    return {
        "Promedio": promedio, 
        "Estado": estado,
        "Recomendacion": recomendacion
    }

"""
Endpionts
"""

@app.get("/")
def inicio ():
    return {"mensaje" : "Servidor Inteligente de calificaciones"}

@app.post("/estudiantes/")
def agregar_estudiante(estudiante: Estudiante):
    db.append(estudiante)
    return {"mensaje": "Estudiante agregado":}
 
@app.get("//")