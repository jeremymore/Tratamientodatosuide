# 🎓 Proyecto Maestría – UIDE

---

## 📋 Descripción General

Proyecto desarrollado para la Maestría en la Universidad Internacional del Ecuador (UIDE), que abarca la construcción de una API REST, uso de control de versiones con branches, contenerización con Docker y pruebas funcionales con `curl`.

---

## Parte 1 – Construcción del API

### 🔵 Endpoint GET

El endpoint GET permite consultar recursos existentes del sistema y retorna las respuestas en formato JSON.

![Endpoint GET](https://github.com/user-attachments/assets/29610765-5726-4910-805e-901225fad8c2)

---

### 🟢 Endpoint POST

El endpoint POST permite crear nuevos recursos en el sistema enviando datos en el cuerpo de la petición.

![Endpoint POST](https://github.com/user-attachments/assets/e50590e6-ec4b-48a0-99d1-17429115d8ed)

#### ✅ Validación básica de datos

Se implementó validación de los campos requeridos antes de procesar la solicitud.

![Validación de datos](https://github.com/user-attachments/assets/4aa5fe2b-3a19-4009-9896-e0082ebe2ded)

#### 📦 Respuestas en formato JSON

Todas las respuestas de la API son retornadas en formato JSON estructurado.

![Respuestas JSON](https://github.com/user-attachments/assets/726a398b-f0d5-40bd-9a09-10b5d1b9ff26)

---

## Parte 2 – Uso de Branches

La gestión del código fuente se realizó utilizando **Git Flow** con branches separadas por funcionalidad.

**Flujo de trabajo:**

1. Se creó una branch nueva para desarrollar la funcionalidad.
2. Se realizaron los commits correspondientes en dicha branch.
3. Se hizo **merge** a la branch `main` una vez validada la funcionalidad.

> 💡 Al menos una funcionalidad fue desarrollada en una branch independiente antes de integrarse a `main`.

---

## Parte 3 – Contenerización

El proyecto fue contenerizado utilizando **Docker**, garantizando portabilidad y reproducibilidad del entorno.

### 🐳 Construcción de la imagen

La imagen se construye sin errores ejecutando el siguiente comando:

```bash
docker build -t mi-fastapi .
```

![Docker Build](https://github.com/user-attachments/assets/5724b19d-7e63-4ed6-814a-c127bbc53c86)

### ▶️ Ejecución del contenedor

El contenedor ejecuta correctamente el API en el puerto configurado:

```bash
 docker run -d -p 8000:8000 mi-fastapi
```

![Docker Run](https://github.com/user-attachments/assets/70dac5b6-8c91-48e7-8651-50b13f08307e)

---

## Parte 4 – Pruebas con `curl`

Se realizaron pruebas funcionales directamente desde la terminal utilizando el comando `curl`.

### 🔵 GET funcionando

```bash
curl -X 'GET' \
  'http://localhost:8000/notas/' \
  -H 'accept: application/json'
```

![Prueba GET](https://github.com/user-attachments/assets/5e05d5c8-e382-429c-9de1-6c720c55c673)

---

### 🟢 POST funcionando

```bash
curl -X 'POST' \
  'http://localhost:8000/notas/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "id": 1,
  "titulo": "jeremy notas",
  "contenido": "esto es una prueba",
  "completada": false,
  "fecha_inicio": "2026-03-24T03:19:52.515Z",
  "fecha_fin": "2026-03-24T03:19:52.515Z"
}'
```

![Prueba POST](https://github.com/user-attachments/assets/e36281e2-6a2e-4bfb-ba54-345cf7356562)

---

### ⚠️ Manejo de errores

Se verificaron los distintos escenarios de error que retorna el API:

**Error por datos inválidos o faltantes:**

![Error 1](https://github.com/user-attachments/assets/d6f19183-27d9-4a77-93ff-0b1f6955c654)

**Error por recurso no encontrado:**

![Error 2](https://github.com/user-attachments/assets/b4c94b5a-a95e-43b5-9754-ab451d13621c)

**Error por solicitud incorrecta:**

![Error 3](https://github.com/user-attachments/assets/7693eef6-1abe-4ee0-9eb4-ac0a48746903)

---

