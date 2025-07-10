from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from config.database import get_connection, SessionLocal

Base = declarative_base()

class Utilisateur(Base):
    __tablename__ = "Utilisateur"
    Id_User = Column(Integer, primary_key=True, autoincrement=True)
    Nom = Column(String(50), nullable=False)
    Prenom = Column(String(50), nullable=False)
    Lieu = Column(String(50), nullable=False)

    def __repr__(self):
        return f"<Utilisateur(Id_User={self.Id_User}, Nom='{self.Nom}', Prenom='{self.Prenom}', Lieu='{self.Lieu}')>"

    def create_user(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO utilisateur (nom, prenom, lieu) VALUES (?)",
            (self.nom,)
        )
        conn.commit()
        self.id = cursor.lastrowid
        conn.close()

    def get_user(self, id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM utilisateur WHERE id = ?",
            (id,)
        )
        row = cursor.fetchone()
        conn.close()
        if row:
            self.id, self.nom = row
            return self
        return None

    @staticmethod
    def get_all_users():
        db = SessionLocal()
        try:
            return db.query(Utilisateur).all()
        finally:
            db.close()

    def update_user(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE utilisateur SET nom = ? WHERE id = ?",
            (self.nom, self.id)
        )
        conn.commit()
        conn.close()

    def delete_user(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "DELETE FROM utilisateur WHERE id = ?",
            (self.id,)
        )
        conn.commit()
        conn.close()