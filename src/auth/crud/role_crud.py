from sqlalchemy.orm import Session

from auth.models import RoleModel
from auth.schemas.role_schema import RoleInSchema


def get_roles(session: Session, skip: int = 0, limit: int = 100):
    return session.query(RoleModel).offset(skip).limit(limit).all()


def get_role(session: Session, role_name: str):
    return session.query(RoleModel).filter(RoleModel.name == role_name).first()


def create_role(session: Session, role: RoleInSchema):
    role_db = RoleModel(**role.__dict__)

    session.add(role_db)
    session.commit()
    session.refresh(role_db)

    return role_db


def get_or_create_role(session: Session, role_name: str):
    role = get_role(session, role_name)

    if role is None:
        role = create_role(session, RoleInSchema(name=role_name))

    return role
