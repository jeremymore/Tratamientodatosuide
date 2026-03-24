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

@app.put("/notas/{nota_id}")
def actualizar_nota(nota_id: int, nota_actualizada: Nota):
    for index, n in enumerate(notas_db):
        if n["id"] == nota_id:
            notas_db[index] = nota_actualizada.dict()
            return {"mensaje": "Nota actualizada con éxito", "nota": notas_db[index]}
    
    # Si termina el ciclo y no encontró el ID, lanza un error 404
    raise HTTPException(status_code=404, detail="Nota no encontrada")

@app.delete("/notas/{nota_id}")
def eliminar_nota(nota_id: int):
    for index, n in enumerate(notas_db):
        if n["id"] == nota_id:
            nota_eliminada = notas_db.pop(index)
            return {"mensaje": "Nota eliminada con éxito", "nota": nota_eliminada}
            
    raise HTTPException(status_code=404, detail="Nota no encontrada")
