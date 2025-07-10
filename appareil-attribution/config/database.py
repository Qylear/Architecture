from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

MYSQL_USER = "root"
MYSQL_PASSWORD = "galerapass"
MYSQL_HOST = "localhost"  # <-- connexion depuis Windows
MYSQL_PORT = "3306"       # <-- port exposé par galera1
MYSQL_DB = "attribution"

DATABASE_URL = (
    f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}"
)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_connection():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()