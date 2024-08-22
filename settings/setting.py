from dotenv import load_dotenv
import os

load_dotenv()

EMAIL = os.getenv('EMAIL')
SENHA = os.getenv('SENHA')
SECRET_KEY = os.getenv('SECRET_KEY')
