from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

app = FastAPI()

# Base de datos en memoria
notas_db = []

# Modelo de datos con fechas
class Nota(BaseModel):
    id: int
    titulo: str
    contenido: str
    completada: bool = False
    fecha_inicio: datetime  # Obligatorio
    fecha_fin: Optional[datetime] = None  # Opcional

@app.post("/notas/")
def crear_nota(nota: Nota):
    # Guardamos la nota (convertimos a diccionario para la lista)
    nueva_nota = nota.dict()
    notas_db.append(nueva_nota)
    return {"mensaje": "Nota creada con éxito", "nota": nueva_nota}

@app.get("/notas/", response_model=List[Nota])
def obtener_notas():
    return notas_db