from ninja.orm import create_schema
from ninja import Schema
from .models import User

UserSchema = create_schema(User)

class UserSchemaOut(Schema):
    id: int
    username: str = None
    first_name: str = None
    last_name: str = None
    email: str = None

class UserSchemaIn(Schema):
    id: int

class UserSchemaAuth(Schema):
    email: str
    password: str