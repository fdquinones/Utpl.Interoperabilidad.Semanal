from fastapi import FastAPI

app = FastAPI()

# Datos de ejemplo para productos
productos = [
    {"id": 1, "nombre": "Producto 1", "precio": 10.99},
    {"id": 2, "nombre": "Producto 2", "precio": 19.99},
    {"id": 3, "nombre": "Producto 3", "precio": 5.99},
    {"id": 4, "nombre": "Producto 4", "precio": 5.99},
    {"id": 5, "nombre": "Producto 5", "precio": 5.99},
]

@app.get("/productos")
async def listar_productos():
    return productos