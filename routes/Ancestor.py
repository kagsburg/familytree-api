
from fastapi import APIRouter, Body

from models.Ancestor import Ancestor
from config.db import conn
from schemas.ancestor import ancestorEntity, serializeList
from bson import ObjectId
ancestor = APIRouter()

@ancestor.get('/ancestors')
async def get_ancestors():
    # ancestors = conn.db.ancestors.find()
    ancestor = conn.local.collection.find()
    print(ancestor)
    return list(ancestor)

# function to get only ancestor 
@ancestor.get('/ancestor')
async def get_ancestor():
    ancestor = conn.local.collection.find({'parent': None })
    return serializeList(ancestor)
# function to add new ancestor
@ancestor.post('/ancestor')
async def add_ancestor(ancestor: Ancestor = Body(...)):
    ancestor.id = ancestor.name
    result =  conn.local.collection.insert_one(dict(ancestor))
    # get inserted id 

    return serializeList(conn.local.collection.find({'_id': ObjectId(result.inserted_id)}))

    # function to get only ancestor
@ancestor.get('/ancestor/{id}')
async def get_ancestor(id: str):
    ancestor = conn.local.collection.find({'_id': ObjectId(id) })
    return serializeList(ancestor)

    # function to update ancestor 
@ancestor.put('/ancestor/{id}')
async def update_ancestor(id: str, ancestor: Ancestor):
    ancestor.id = ancestor.name
    conn.local.collection.update_one({'_id': ObjectId(id)}, {'$set': dict(ancestor)})    
    return serializeList(conn.local.collection.find({'_id': ObjectId(id)}))

    # function to delete ancestor
@ancestor.delete('/ancestor/{id}')
async def delete_ancestor(id: str):
    conn.local.collection.delete_one({'_id': ObjectId(id)})
    return serializeList(conn.local.collection.find())

# get all children of an ancestor
@ancestor.get('/ancestor/{id}/children')
async def get_ancestor_children(id: str):
    ancestor = conn.local.collection
    ancestor = ancestor.find({'_id': ObjectId(id)})
    ancestor = serializeList(ancestor)
    ancestor = ancestor[0]
    children = conn.local.collection
    children = children.find({'parent': ancestor['name']})
    return serializeList(children)

