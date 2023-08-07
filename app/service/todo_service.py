from dto.todo_schema import ToDo
from datetime import datetime

todo_list = []
final_todo_list = []

formatting_datetime = str(datetime.now().strftime("%d-%m-%y %H:%M:%S"))

def create_todo(payload: dict):
    data = ToDo(
        id=0,
        title= payload.title,
        description=payload.description,
        created_at=formatting_datetime
    )
    todo_list.append(data)
    id = len(todo_list)
    data = data.copy(update={'id':id})
    final_todo_list.append(data)
    return data

def get_all_todo():
    return final_todo_list

def get_todo_by_id(id:int):
    data = [data for data in final_todo_list if data.id == int(id)]
    return data

def update_todo(id:int, payload:dict):
    for data in final_todo_list:
        if data.id == int(id):
            updated_data = ToDo(
                id=data.id,
                title=payload.title,
                description=payload.description,
                finished_at=data.finished_at,
                created_at=data.created_at,
                updated_at=formatting_datetime,
                deleted_at=data.deleted_at,
                status="active"
            )
    
    data = [final_todo_list.remove(data) for data in final_todo_list if data.id == int(id)]
    final_todo_list.append(updated_data)
    
    return updated_data

def finish_todo(id:int):
    for data in final_todo_list:
        if data.id == int(id):
            finish_data = ToDo(
                id=data.id,
                title=data.title,
                description=data.description,
                finished_at=formatting_datetime,
                created_at=data.created_at,
                updated_at=data.updated_at,
                deleted_at=data.deleted_at,
                status="finished"
            )
    
    data = [final_todo_list.remove(data) for data in final_todo_list if data.id == int(id)]
    final_todo_list.append(finish_data)
    
    return finish_data

def delete_todo(id:int):
    for data in final_todo_list:
        if data.id == int(id):
            deleted_data = ToDo(
                id=data.id,
                title=data.title,
                description=data.description,
                finished_at=data.finished_at,
                created_at=data.created_at,
                updated_at=data.updated_at,
                deleted_at=formatting_datetime,
                status="deleted"
            )
    
    data = [final_todo_list.remove(data) for data in final_todo_list if data.id == int(id)]
    final_todo_list.append(deleted_data)
    
    return deleted_data