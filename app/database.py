from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os , psycopg2 
engine = os.getenv('DATABASE_URL')
if not engine:
    engine = create_engine('postgresql+psycopg2://DB_USER:DB_PASSWORD@DB_HOST/DB_NAME')

db = SQLAlchemy()
load_dotenv()

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f"<User {self.username}>"

