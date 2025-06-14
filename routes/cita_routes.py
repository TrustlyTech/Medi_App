from flask import Blueprint, request, jsonify
from models import Cita
from db import db

cita_bp = Blueprint('cita', __name__)

@cita_bp.route('/citas', methods=['POST'])
def crear_cita():
    data = request.json
    nueva_cita = Cita(
        usuario_id=data['usuario_id'],
        fecha=data['fecha'],
        doctor=data['doctor'],
        motivo=data['motivo']
    )
    db.session.add(nueva_cita)
    db.session.commit()
    return jsonify({"mensaje": "Cita registrada correctamente"}), 201

@cita_bp.route('/citas/<int:usuario_id>', methods=['GET'])
def obtener_citas(usuario_id):
    citas = Cita.query.filter_by(usuario_id=usuario_id).all()
    return jsonify([
        {
            "fecha": c.fecha,
            "doctor": c.doctor,
            "motivo": c.motivo
        } for c in citas
    ])
