from datetime import date
from flask import request, jsonify
from app.models.attribuer import Attribuer
from app.models.utilisateur import Utilisateur
from app.models.appareil import Appareil

class AttributionController:
    def allocate_device(self):
        data = request.json
        id_utilisateur = data.get('id_utilisateur')
        id_appareil = data.get('id_appareil')
        
        # Logic to allocate device
        allocation = Attribuer(id_appareil=id_appareil, id_utilisateur=id_utilisateur)
        allocation.create()  # Assuming create method saves the allocation to the database
        
        return jsonify({"message": "Device allocated successfully", "allocation": allocation}), 201

    def return_device(self):
        data = request.json
        id_utilisateur = data.get('id_utilisateur')
        id_appareil = data.get('id_appareil')
        
        # Logic to return device
        allocation = Attribuer.retrieve(id_utilisateur, id_appareil)  # Assuming retrieve method fetches the allocation
        if allocation:
            allocation.date_restitution = date.today()  # Assuming date is imported
            allocation.update()  # Assuming update method saves the changes to the database
            
            return jsonify({"message": "Device returned successfully", "allocation": allocation}), 200
        else:
            return jsonify({"message": "No allocation found for this device and user"}), 404