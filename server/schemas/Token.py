from pydantic import BaseModel
from typing import Optional


class Token(BaseModel):
    """
    Returned Token content.
    """
    access_token: str = None
    token_type: str = None


class TokenData(BaseModel):
    """
    Access token content.
    """
    user_id: Optional[str] = None
    user_name: Optional[str] = None
    is_admin: Optional[str] = None
    exp: Optional[str] = None
