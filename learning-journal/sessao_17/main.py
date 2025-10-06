from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def ler_raiz():
    return {"message": "Testando primeira API!"}

@app.get("/items/{item_id}")
def ler_item(item_id: int):
    return {"item_id": item_id, "description": f"Você buscou o item número {item_id}"}