from typing import Optional

from pydantic import BaseModel, Field

class Ancestor(BaseModel):
    id: str= None 
    name: str = Field(...)
    image: str= Field(...)
    spouse: object= Field(...)
    parent: str = None
    status: bool = Field(...)

    
    class Config:
        schema_extra = {
            "example": {
                "name": "John Doe",
                "image": "user.png",
                "spouse": {"name": "Jane Doe", "image": "user.png"},
                "parent": None,
                "status": "true",
            }
        }
class UpdateAncestorModel(BaseModel):
    name: Optional[str]
    image: Optional[str]
    spouse: Optional[object]
    parent: Optional[str]
    status: Optional[bool]
    

    class Config:
        schema_extra = {
            "example": {
                "name": "John Doe",
                "image": "user.png",
                "spouse": {"name": "Jane Doe", "image": "user.png"},
                "parent": None,
                "status": "true",
            }
        }

def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }

def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}