from pydantic import BaseModel


class Todo(BaseModel):
    name: str
    id:str
    department: str
