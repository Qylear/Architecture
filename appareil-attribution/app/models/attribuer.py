from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base
from config.database import SessionLocal

Base = declarative_base()

class Attribuer(Base):
    __tablename__ = "attribuer"
    Id_Appareil = Column(Integer, ForeignKey("Appareil.Id_appareil"), primary_key=True)
    Id_Utilisateur = Column(Integer, ForeignKey("Utilisateur.Id_User"), primary_key=True)
    Id_Enrolement = Column(Integer, ForeignKey("Enrolement.Id_Enrolement"), primary_key=True)
    date_attribution = Column(DateTime, nullable=True)
    date_restitution = Column(DateTime, nullable=True)

    def __repr__(self):
        return (
            f"<Attribuer(Id_Appareil={self.Id_Appareil}, "
            f"Id_Utilisateur={self.Id_Utilisateur}, "
            f"Id_Enrolement={self.Id_Enrolement}, "
            f"date_attribution={self.date_attribution}, "
            f"date_restitution={self.date_restitution})>"
        )

    @staticmethod
    def create(id_appareil, id_utilisateur, id_enrolement, date_attribution=None, date_restitution=None):
        db = SessionLocal()
        try:
            allocation = Attribuer(
                Id_Appareil=id_appareil,
                Id_Utilisateur=id_utilisateur,
                Id_Enrolement=id_enrolement,
                date_attribution=date_attribution,
                date_restitution=date_restitution
            )
            db.add(allocation)
            db.commit()
            return allocation
        finally:
            db.close()

    @staticmethod
    def get_all_allocations():
        db = SessionLocal()
        try:
            return db.query(Attribuer).all()
        finally:
            db.close()

    @staticmethod
    def get_allocation_by_id(id_appareil, id_utilisateur, id_enrolement):
        db = SessionLocal()
        try:
            return db.query(Attribuer).filter_by(
                Id_Appareil=id_appareil,
                Id_Utilisateur=id_utilisateur,
                Id_Enrolement=id_enrolement
            ).first()
        finally:
            db.close()