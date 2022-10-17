# Takes the output file of people and sends to database py
import asyncio
from unittest import async_case
from pydantic import BaseModel
import database
from motor.motor_asyncio import AsyncIOMotorClient

# Getting the client loop from database
client = database.client
client.get_io_loop = asyncio.get_event_loop


class DataUpdate:
    # Name empty so can be deleted
    def __init__(self, name='empty', id='', dept=''):
        # Skips the entry
        self.NoRun = False
        # Dict to be added to MongoDB
        self.reggie = {"name": name, "id": id, "department": dept}
        
        asyncio.run(DataUpdate.function_asyc(self.reggie, asyncio.run(DataUpdate.chckDouble(name, self.NoRun))))
    # Formatting for json config

    async def chckDouble(name, NoRun):
        duplicate = await database.fetch_one_todo(name)
        if duplicate is None:  # If name exists dont make an entry
            return NoRun
        else:
            NoRun = True
            return NoRun
    #    for k,v in enumerate(duplicate.items()):
     #       print(k,v)

    async def function_asyc(upload, NoRun):
        if NoRun is False:
            await database.create_todo(upload)


if __name__ in "__main__":
    # Run line
    upload = DataUpdate(name='empty', id='', dept='')
