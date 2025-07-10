from flask import render_template, request, redirect, url_for
from app.models.attribuer import Attribuer
from app.models.utilisateur import Utilisateur
from app.models.appareil import Appareil
from app.models.enrolement import Enrolement
from config.database import SessionLocal

def display_allocation_form():
    utilisateurs = Utilisateur.get_all_users()
    appareils = Appareil.get_all_apareils()
    enrolement = Enrolement.get_all_enrolements()
    return render_template('allocation_form.html', utilisateurs=utilisateurs, appareils=appareils, enrolements=enrolement)


def display_allocation_status(allocation_id):
    attribuer = Attribuer.get_allocation_by_id(allocation_id)
    return render_template('allocation_status.html', allocation=attribuer)


def submit_allocation_form():
    id_utilisateur = request.form.get('utilisateur')
    id_appareil = request.form.get('appareil')
    id_enrolement = request.form.get('enrolement')

    db = SessionLocal()
    attribution = Attribuer(
        Id_Appareil=int(id_appareil),
        Id_Utilisateur=int(id_utilisateur),
        Id_Enrolement=int(id_enrolement)
    )
    db.add(attribution)
    db.commit()
    db.close()
    return redirect(url_for('allocation_form'))