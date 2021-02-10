"""
Файл конфигурации фласка
"""

from cryptography.fernet import Fernet


class Config:
    SECRET_KEY = Fernet.generate_key()
