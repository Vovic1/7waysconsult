from fastapi import FastAPI
from type_lib import poll
import db as db

app = FastAPI()

@app.get("/")
async def root():
    print("app.get->db.poll_table")
    return db.poll_table()

@app.get("/poll/{id}")
async def poll_by_id(id: int):
    return  db.poll_by_id(id)

@app.get("/poll/{id}/act/{a}")
async def poll_status(id: int, a:bool):
    return  db.poll_status(id, a)
    

@app.post("/poll")
async def poll_add(p: poll):
    #print("name = %s , descr = %s..." % (p.name, p.descr))
    resp = db.poll_add(p)
    print("resp = %r " % (resp,))
    return resp

@app.put("/poll/{id}")
def poll_upd(id: int, p: poll):
    return db.poll_upd(id, p)
