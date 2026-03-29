from pydantic import BaseModel, Field, field_validator

class UserCreate(BaseModel):
    username: str = Field(
        ...,
        min_length=3,
        max_length=20,
        pattern="^[a-zA-Z][a-zA-Z0-9_]{2,19}$"
    )

    password: str = Field(
        ...,
        min_length=6,
        max_length=50
    )

    @field_validator('password')
    @classmethod
    def validate_password(cls, v):
        if not any(c.islower() for c in v):
            raise ValueError('Password must contain at least one lowercase letter')
        if not any(c.isupper() for c in v):
            raise ValueError('Password must contain at least one uppercase letter')
        if not any(c.isdigit() for c in v):
            raise ValueError('Password must contain at least one digit')
        if not any(c in '@$!%*?&' for c in v):
            raise ValueError('Password must contain at least one special character (@$!%*?&)')
        return v


class UserLogin(BaseModel):
    username: str = Field(
        ...,
        min_length=3,
        max_length=20
    )

    password: str = Field(
        ...,
        min_length=6,
        max_length=50
    )