from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'uma-chave-segura')
    FATSECRET_CLIENT_ID = os.getenv('FATSECRET_CLIENT_ID')
    FATSECRET_CLIENT_SECRET = os.getenv('FATSECRET_CLIENT_SECRET')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///meals.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
