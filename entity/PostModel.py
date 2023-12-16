from datetime import datetime
from pydantic import BaseModel

class PostModel(BaseModel):
    def __init__(self, id: int, name: str, writer: str, main: str):
        self.id = id
        self.name = name
        self.date = datetime.now()
        self.writer = writer
        self.main = main

    def __str__(self):
        return f"Post(id={self.id}, name='{self.name}', date={self.date}, writer='{self.writer}', main='{self.main}')"
    

    def change(self, id: int, name: str, main: str):
        self.id = id
        self.name = name
        self.date = datetime.now()
        self.main = main

    
