# import from actual folder to fill __init__
from .config import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER, TOKEN

__all__ = [
    'DB_HOST',
    'DB_NAME',
    'DB_PASS',
    'DB_PORT',
    'DB_USER',
    'TOKEN'
]
