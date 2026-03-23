from fastapi import FastAPI
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
#GET 2 PARTE 
from fastapi import Query, HTTPException
# GET ALL NOTES
@app.get("/notas/", response_model=List[Nota])
def obtener_notas(
    completada: Optional[bool] = Query(None, description="Filtrar por estado"),
    skip: int = 0,
    limit: int = 10
):

    resultado = notas_db

    # Filtro por estado (pendiente/completado)
    if completada is not None:
        resultado = [n for n in resultado if n["completada"] == completada]

    # Paginación
    return resultado[skip: skip + limit]



# GET NOTE DETAILS (por ID)

@app.get("/notas/{nota_id}", response_model=Nota)
def obtener_detalle_nota(nota_id: int):

    for nota in notas_db:
        if nota["id"] == nota_id:
            return nota

    raise HTTPException(
        status_code=404,
        detail="Nota no encontrada"
    )
