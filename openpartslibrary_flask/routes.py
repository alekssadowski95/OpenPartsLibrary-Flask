from flask import request, jsonify, Flask, url_for
from openpartslibrary.db import PartsLibrary
from openpartslibrary.models import Part
import os
import uuid

app = Flask(__name__)

db_path = os.path.join(app.static_folder, 'parts.db')
p1 = PartsLibrary(db_path)

@app.route("/")
def index():
    db_url = url_for('static', filename='parts.db')
    return f"Database URL for download: <a href='{db_url}'>{db_url}</a>"

p1.delete_all()
sample_path = os.path.join(os.path.dirname(__file__),'openpartslibrary_flask', 'parts_data_sample.xlsx')
p1.create_parts_from_spreadsheet(sample_path)

#Adding parts
new_part = Part(
            number='SCRW-2001',
            name='Screw Type Z (Special) M5x14',
            description='A special kind of screw for safety switches',
            revision="1",
            lifecycle_state="In Work",
            owner='Max Mustermann',
            material='Steel',
            mass=0.03,
            dimension_x=0.02,
            dimension_y=0.005,
            dimension_z=0.005,
            quantity=100,
            cad_reference='CAD REFERENCE',
            attached_documents_reference='DOCUMENTS REFERENCE',
            lead_time=10,
            make_or_buy='make',
            supplier='In-House Manufacturing',
            manufacturer_number='MFN-100001',
            unit_price=0.45,
            currency='EUR'
        )
#Add 3 more parts
new_part2 = Part(
            uuid=str(uuid.uuid4()),
            number='BOLT-2002',
            name='Hex Bolt',
            description='A standard hex bolt',
            revision="1",
            lifecycle_state="In Work",
            owner="Portland Bolt",
            material='Stainless Steel',
            mass=0.05,
            dimension_x=0.03,
            dimension_y=0.01,
            dimension_z=0.01,
            quantity=150,
            cad_reference='CAD REFERENCE BOLT',
            attached_documents_reference='DOCUMENTS REFERENCE BOLT',
            lead_time=7,    
            make_or_buy='buy',
            supplier='Portland Bolt',
            manufacturer_number='PB-2002',
            unit_price=0.75,    
            currency='EUR'
        )
new_part3 = Part(
            uuid=str(uuid.uuid4()),
            number='BOLT-2003',
            name='Carriage Bolt',
            description='A standard carriage bolt',
            revision="1",
            lifecycle_state="In Work",
            owner="Fastenal",
            material='Carbon Steel',
            mass=0.04,
            dimension_x=0.025,
            dimension_y=0.008,
            dimension_z=0.008,
            quantity=200,
            cad_reference='CAD REFERENCE CARRIAGE BOLT',
            attached_documents_reference='DOCUMENTS REFERENCE CARRIAGE BOLT',
            lead_time=5,
            make_or_buy='buy',
            supplier='Fastenal',
            manufacturer_number='FB-3003',
            unit_price=0.60,
            currency='EUR'
)
new_part4 = Part(
            uuid=str(uuid.uuid4()),
            number='NUT-2004',
            name='Hex Nut',     
            description='A standard hex nut',
            revision="1",
            lifecycle_state="In Work",
            owner="Grainger",
            material='Brass',
            mass=0.02,
            dimension_x=0.015,
            dimension_y=0.007,
            dimension_z=0.007,
            quantity=300,
            cad_reference='CAD REFERENCE HEX NUT',
            attached_documents_reference='DOCUMENTS REFERENCE HEX NUT',
            lead_time=4,
            make_or_buy='buy',
            supplier='Grainger',
            manufacturer_number='GN-4004',
            unit_price=0.30,
            currency='EUR'
)
p1.session.add(new_part)
p1.session.add(new_part2)
p1.session.add(new_part3)
p1.session.add(new_part4)
p1.session.commit()

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

class Routes:
    def __init__(self, app):
        self.app = app
        self.register_routes()

    def register_routes(self):
        @self.app.route('/')
        def home():
            return 'OpenPartsLibrary Flask API is running!'
        
        @self.app.route('/api/create-part', methods=['POST'])
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
        
        #Reading part by number
        @self.app.route('/api/read-part/<string:number>', methods=['GET'])
        def api_read_part(number):
            part = p1.session.query(Part).filter(Part.number == number).first()
            if part is None:
                return jsonify({'error': 'Part not found'}), 404
            return jsonify(part_to_dict(part))
        
        #Updating part by number
        @self.app.route('/api/update-part/<string:number>', methods=['PUT'])
        def api_update_part(number):
            part = p1.session.query(Part).filter(Part.number == number).first()
            if part is None:
                return jsonify({'error': 'Part not found'}), 404
            data = request.get_json()
            for field in data:
                if hasattr(part, field):
                    setattr(part, field, data[field])
            p1.session.commit()
            return jsonify(part_to_dict(part))
        
        #Deleting part by number
        @self.app.route('/api/delete-part/<string:number>', methods=['DELETE'])
        def api_delete_part(number):
            part = p1.session.query(Part).filter(Part.number == number).first()
            if part is None:
                return jsonify({'error': 'Part not found'}), 404
            p1.session.delete(part)
            p1.session.commit()
            return jsonify({"message" : f"Part {number} deleted successfully."})
        
        #Reading all parts
        @self.app.route('/api/read-all-parts', methods=['GET'])
        def api_read_all_parts():
            parts = p1.session.query(Part).all()
            return jsonify([part_to_dict(p) for p in parts])

Routes(app)

if __name__ == '__main__':
    app.run(debug=True)
        
        