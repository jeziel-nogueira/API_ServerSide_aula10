from flask import jsonify, request, abort
from app import db
from app.models import Client
from app.routes import bp
from app.auth import token_required

@bp.route('/clients', methods=['GET'])
@token_required
def get_clients(current_user):
    client_id = request.args.get('client_id')

    if client_id:
        try:
            client = Client.query.get_or_404(client_id)
            return jsonify(client.to_dict()),200
        except Exception as e:
            return jsonify({'Error': str(e)}), 500
    else:
        try:
            clients = Client.query.all()
            return jsonify([clients.to_dict() for client in clients]),200
        except Exception as e:
            return jsonify({'Error': str(e)}), 500
        
@bp.route('/clients', methods=['GET'])
@token_required
def create_client(current_user):
    try:
        data = request.get_json() or {}
        if 'name' not in data or 'email' not in data:
            return jsonify({'message': 'Name and email are required'}), 400
        if Client.query.filter_by(name=data['name']).first():
            return jsonify({'message': 'Name already registered'}), 400
        if Client.query.filter_by(email=data['email']).first():
            return jsonify({'message': 'Email already registered'}), 400
        
        client = Client(name=data['name'], email=data['email'])
        db.session.add(client)
        db.session.commit()
        return jsonify(client.to_dict()), 201
    except Exception as e:
        return jsonify({'Error': str(e)}), 500
