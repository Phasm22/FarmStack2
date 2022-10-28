
import motor.motor_asyncio
from model import Todo

client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017/')
database = client.TodoList
collection = database.Todo


async def fetch_one_todo(name):
    document = await collection.find_one({"name": name})
    return document


async def fetch_all_todos():
    todos = []
    cursor = collection.find({})
    async for document in cursor:
        todos.append(Todo(**document))
    return todos


async def create_todo(todo):
    document = todo
    result = await collection.insert_one(document)
    return document


async def update_todo(name, dept):
    await collection.update_one({"name": name}, {"$set": {"department": dept}})
    document = await collection.find_one({"name": name})
    return document


async def remove_todo(name):
    await collection.delete_one({"name": name})
    return True
