from pydantic import BaseModel, Field, EmailStr

class SearchSchema(BaseModel):
    cedula: str = Field(..., example="123456789", min_length=1, max_length=50)
    # email: EmailStr = Field(..., example="alanturing@enigmasas.com")
    # phone: str = Field(..., example="1234567890", min_length=7, max_length=15)