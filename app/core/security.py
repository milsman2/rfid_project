"""Cryptography package import"""
from passlib.context import CryptContext


PWD_CONTEXT = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Use cryptography to verify password hash"""
    return PWD_CONTEXT.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    """Return hashed password"""
    return PWD_CONTEXT.hash(password)
