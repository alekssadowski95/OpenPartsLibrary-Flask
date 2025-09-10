from flask import request, jsonify, url_for, app
from openpartslibrary.db import PartsLibrary
from openpartslibrary.models import Part
import os

from . import app

db_path = os.path.join(app.static_folder, 'parts.db')
p1 = PartsLibrary()


def part_to_dict(part):
    return {
        'uuid': part.uuid,
        'number': part.number,
        'name': part.name,
        'description': part.description,
        'revision': part.revision,
        'lifecycle_state': part.lifecycle_state,
        'owner': part.owner,
        'material': part.material,
        'mass': part.mass,
        'dimension_x': part.dimension_x,
        'dimension_y': part.dimension_y,
        'dimension_z': part.dimension_z,
        'quantity': part.quantity,
        'cad_reference': part.cad_reference,
        'attached_documents_reference': part.attached_documents_reference,
        'lead_time': part.lead_time,
        'make_or_buy': part.make_or_buy,
        'supplier': part.supplier,
        'manufacturer_number': part.manufacturer_number,
        'unit_price': part.unit_price,
        'currency': part.currency
    }

@app.route('/')
def index():
    db_url = url_for('static', filename='parts.db')
    return f"Database URL for download: <a href='{db_url}'>{db_url}</a>"

@app.route('/api/create-part', methods=['POST'])
def api_create_part():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Invalid input'}), 400
    part = Part(
        number=data.get('number'),
        name=data.get('name'),
        description=data.get('description'),
        revision=data.get('revision'),
        lifecycle_state=data.get('lifecycle_state'),
        owner=data.get('owner'),
        material=data.get('material'),
        mass=data.get('mass'),
        dimension_x=data.get('dimension_x'),
        dimension_y=data.get('dimension_y'),
        dimension_z=data.get('dimension_z'),
        quantity=data.get('quantity'),
        cad_reference=data.get('cad_reference'),
        attached_documents_reference=data.get('attached_documents_reference'),
        lead_time=data.get('lead_time'),
        make_or_buy=data.get('make_or_buy'),
        supplier=data.get('supplier'),
        manufacturer_number=data.get('manufacturer_number'),
        unit_price=data.get('unit_price'),
        currency=data.get('currency')
    )
    p1.session.add(part)
    p1.session.commit()
    return jsonify(part_to_dict(part)), 201

@app.route('/api/read-part/<string:number>', methods=['GET'])
def api_read_part(number):
    part = p1.session.query(Part).filter(Part.number ==number).first()
    if not part:
        return jsonify({'error': 'Part not found'}), 404
    return jsonify(part_to_dict(part))

@app.route('/api/update-part/<string:number>', methods=['PUT'])
def api_update_part(number):
    part = p1.session.query(Part).filter(Part.number ==number).first()
    if not part:
        return jsonify({'error': 'Part not found'}), 404
    data = request.get_json()
    for field in data:
        if hasattr(part, field):
            setattr(part, field, data[field])
    p1.session.commit()
    return jsonify(part_to_dict(part))

@app.route('/api/delete-part/<string:number>', methods=['DELETE'])
def api_delete_part(number):
    part = p1.session.query(Part).filter(Part.number ==number).first()
    if not part:
        return jsonify({'error': 'Part not found'}), 404
    p1.session.delete(part)
    p1.session.commit()
    return jsonify({"message" : f"Part {number} deleted successfully"})

@app.route('/api/read-all-parts', methods=['GET'])
def api_read_all_parts():
    parts = p1.session.query(Part).all()
    return jsonify([part_to_dict(part) for part in parts])
    