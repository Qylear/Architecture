from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from config.database import SessionLocal

Base = declarative_base()

class Appareil(Base):
    __tablename__ = "Appareil"
    Id_appareil = Column(Integer, primary_key=True, autoincrement=True)
    Type = Column(String(50), nullable=False)
    Modele = Column(String(50), nullable=False)

    def __repr__(self):
        return f"<Appareil(Id_appareil={self.Id_appareil}, Type='{self.Type}', Modele='{self.Modele}')>"

    @staticmethod
    def get_all_apareils():
        db = SessionLocal()
        try:
            result = db.query(Appareil).all()
            if not result:
                print("Aucun appareil trouvé dans la base de données.")
            else:
                print(f"{len(result)} appareils trouvés : {result}")
            return result
        finally:
            db.close()