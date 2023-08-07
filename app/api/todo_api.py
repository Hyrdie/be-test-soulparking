from fastapi_utils.inferring_router import InferringRouter
from fastapi_utils.cbv import cbv
from .base import BaseApi
from service.todo_service import create_todo, get_all_todo, get_todo_by_id, update_todo, finish_todo, delete_todo
from dto.todo_schema import ToDo
from fastapi.encoders import jsonable_encoder

todo_api = InferringRouter()

@cbv(todo_api)
class ToDo(BaseApi):
    @todo_api.post("/todo", response_model=ToDo)
    async def post_create_todo(self, payload:ToDo):
        data = create_todo(payload)
        return self.make_response(message="success", payload=jsonable_encoder(data), code=200)
    
    @todo_api.get("/todo", response_model=ToDo)
    async def get_all_todo(self):
        data = get_all_todo()
        return self.make_response(message="success", payload=jsonable_encoder(data), code=200)
    
    @todo_api.get("/todo/{id}", response_model=ToDo)
    async def get_todo_by_id(self, id:int):
        data = get_todo_by_id(id)
        return self.make_response(message="success", payload=jsonable_encoder(data), code=200)
    
    @todo_api.put("/todo/{id}", response_model=ToDo)
    async def update_todo(self, id:int, payload:ToDo):
        data = update_todo(id, payload)
        return self.make_response(message="success", payload=jsonable_encoder(data), code=200)
    
    @todo_api.put("/todo/{id}/finish", response_model=ToDo)
    async def finish_todo(self, id:int):
        data = finish_todo(id)
        return self.make_response(message="success", payload=jsonable_encoder(data), code=200)
    
    @todo_api.delete("/todo/{id}", response_model=ToDo)
    async def delete_todo(self, id:int):
        data = delete_todo(id)
        return self.make_response(message="success", payload=jsonable_encoder(data), code=200)