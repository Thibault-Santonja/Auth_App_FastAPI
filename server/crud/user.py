from sqlalchemy.orm import Session
from typing import Optional

from server.db.model_user import User
from server.security.password import verify_password, get_password_hash


def authenticate_user(db: Session, username: str, password: str) -> Optional[User]:
    """
    Verify credentials validity.

    :param db:
    :param username:
    :param password:
    :return:
    """
    user = db.query(User).filter(User.username == username).first()

    if not user:
        # Just to simulate a password checking, prevent timing attack
        verify_password(password, get_password_hash("user.password"))
        return None

    if not verify_password(password, user.password):
        return None

    return user
