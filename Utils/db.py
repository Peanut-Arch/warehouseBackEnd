import asyncpg

DATABASE_CONFIG = {
    'user': 'postgres',
    'password': 'Franco28',
    'database': 'Users',
    'host': 'localhost',
    'port': 5432
}

class Database:
    def __init__(self, config: dict):
        self.config = config
        self.connection = None

    async def connect(self):
        self.connection = await asyncpg.connect(**self.config)

    async def disconnect(self):
        if self.connection:
            await self.connection.close()

    async def fetch(self, query: str, *args):
        if not self.connection:
            raise Exception("Database not connected.")
        return await self.connection.fetch(query, *args)

    async def execute(self, query: str, *args):
        if not self.connection:
            raise Exception("Database not connected.")
        return await self.connection.execute(query, *args)

db = Database(DATABASE_CONFIG)


