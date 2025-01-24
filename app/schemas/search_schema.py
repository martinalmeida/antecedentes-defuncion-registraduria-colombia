from pydantic import BaseModel, Field, EmailStr

class SearchSchema(BaseModel):
    id_card: str = Field(..., example="123456789", min_length=1, max_length=50)
    ip_address: str = Field(..., example="127.0.0.1", min_length=1, max_length=50)
