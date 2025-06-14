from flask import Blueprint, request, jsonify
from models import Usuario
from db import db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/registro', methods=['POST'])
def registrar():
    data = request.json
    nuevo_usuario = Usuario(nombre=data['nombre'], email=data['email'], contraseña=data['contraseña'])
    db.session.add(nuevo_usuario)
    db.session.commit()
    return jsonify({"mensaje": "Usuario registrado"}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    usuario = Usuario.query.filter_by(email=data['email'], contraseña=data['contraseña']).first()
    if usuario:
        return jsonify({"mensaje": "Login exitoso", "usuario_id": usuario.id})
    return jsonify({"error": "Credenciales inválidas"}), 401
