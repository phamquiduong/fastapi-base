from fastapi import status
from sqlalchemy.orm import Session

from auth.crud.user_crud import get_user
from core.helper.password_helper import password_helper
from core.schemas.error_schema import HTTPException


def authenticate_user(db: Session, email: str, password: str):
    user = get_user(db, email=email)

    if not user:
        raise HTTPException(error_code='USR_404')

    if not password_helper.verify(password, user.hashed_password):
        raise HTTPException(error_code='USR_4011')

    return user
