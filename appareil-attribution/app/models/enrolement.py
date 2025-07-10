from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from config.database import get_connection, SessionLocal

Base = declarative_base()

class Enrolement(Base):
    __tablename__ = "Enrolement"
    Id_Enrolement = Column(Integer, primary_key=True, autoincrement=True)
    Lib_Enrolement = Column(String(50), nullable=False)

    def __repr__(self):
        return f"<Enrolement(Id_Enrolement={self.Id_Enrolement}, Lib_Enrolement='{self.Lib_Enrolement}')>"

    @staticmethod
    def get_all_enrolements():
        db = SessionLocal()
        try:
            return db.query(Enrolement).all()
        finally:
            db.close()