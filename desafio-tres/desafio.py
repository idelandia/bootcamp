from fastapi import FastAPI, HTTPException

app = FastAPI()

class Item:
    def __init__(self, id: int, nome: str):
        self.id = id
        self.nome = nome

itens = {1: Item(id=1, nome="Item 1"), 2: Item(id=2, nome="Item 2")}

@app.put("/atualizar_item/{item_id}")
async def atualizar_item(item_id: int, novo_nome: str):
    if item_id not in itens:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    
    item = itens[item_id]
    item.nome = novo_nome
    return {"mensagem": f"Item {item_id} atualizado com sucesso", "novo_nome": novo_nome}

