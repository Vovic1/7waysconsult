from pydantic import BaseModel
class poll(BaseModel):
    id: int
    name: str
    descr: str
    is_act: bool =False
    is_del: bool=False
