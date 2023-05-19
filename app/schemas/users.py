from pydantic import BaseModel, Field
from typing import Union, Optional, List


class UserRequest(BaseModel):
    first_name: str = Field(
        ..., title="First Name", description="First Name of the user"
    )
    last_name: str = Field(..., title="Last Name", description="Last Name of the user")
    email: str = Field(..., title="Email", description="Email of the user")
    password: str = Field(..., title="Password", description="Password of the user")
    phone_number: str = Field(
        ..., title="Phone Number", description="Phone Number of the user"
    )

    class Config:
        schema_extra = {
            "example": {
                "first_name": "John",
                "last_name": "Doe",
                "email": "jd@gmail.com",
                "password": "password",
                "phone_number": "1234567890",
            }
        }
