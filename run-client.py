import requests
import uuid


if __name__ == '__main__':
    print("Starting OpenPartsLibrary Client")

    BASE_URL = "http://localhost:5000"

    new_part_dict = {
        "uuid": str(uuid.uuid4()),
        "number": "SCRW-2001",
        "name": "Screw ISO 4762 M6x12",
        "description": "A hexagon socket head cap screw for fastening metal parts",
        "revision": "1",
        "lifecycle_state": "In Work",
        "owner": "Max Mustermann",
        "material": "Steel",
        "quantity": 100,
        "cad_reference": "CAD REFERENCE",
        "attached_documents_reference": "DOCUMENTS REFERENCE",
        "lead_time": 10,
        "make_or_buy": "buy",
        "supplier": "Adolf Würth GmbH & Co. KG",
        "manufacturer_number": "MFN-100001",
        "unit_price": 0.15,
        "currency": "EUR"
    }
    create_response = requests.post(f"{BASE_URL}/api/create-part", json = new_part_dict)
    print("Create Part Response:", create_response.json())



''' Make sure, that JSON file is safe

def safe_json(response):
    print(f"Response Status Code: {response.status_code}")
    try:
        return response.json()
    except Exception:
        print("Failed to parse JSON response: (status {response.status_code}). Raw response: ")
        print(response.text)
        return None
'''

''' Requests

response = requests.get(f"{BASE_URL}/api/read-all-parts")
print("All Parts:", response.json())

response = requests.get(f"{BASE_URL}/api/read-part/P12345")
print("Read Part Response:", response.json())

update = {"quantity": 150, "unit_price": 11.0}
update_response = requests.put(f"{BASE_URL}/api/update-part/P12345", json=update)
print("Update Part Response:", response.json())

delete_response = requests.delete(f"{BASE_URL}/api/delete-part/P12345")
print("Delete Part Response:", delete_response.json())
'''
        
''' Sample parts

sample_parts = [
    {
        "uuid": str(uuid.uuid4()),
        "number": "SCRW-2001",
        "name": "Screw ISO 4762 M6x12",
        "description": "A hexagon socket head cap screw for fastening metal parts",
        "revision": "1",
        "lifecycle_state": "In Work",
        "owner": "Max Mustermann",
        "material": "Steel",
        "quantity": 100,
        "cad_reference": "CAD REFERENCE",
        "attached_documents_reference": "DOCUMENTS REFERENCE",
        "lead_time": 10,
        "make_or_buy": "buy",
        "supplier": "Adolf Würth GmbH & Co. KG",
        "manufacturer_number": "MFN-100001",
        "unit_price": 0.15,
        "currency": "EUR"
    },
    {
        "uuid": str(uuid.uuid4()),
        "number": "SCRW-2002",
        "name": "Screw ISO 4762 M6x20",
        "description": "A hexagon socket head cap screw for fastening metal parts",
        "revision": "1",
        "lifecycle_state": "In Work",
        "owner": "Max Mustermann",
        "material": "Steel",
        "quantity": 150,
        "cad_reference": "CAD REFERENCE BOLT",
        "attached_documents_reference": "DOCUMENTS REFERENCE BOLT",
        "lead_time": 7,
        "make_or_buy": "buy",
        "supplier": "Adolf Würth GmbH & Co. KG",
        "manufacturer_number": "MFN-100002",
        "unit_price": 0.20,
        "currency": "EUR"
    },
    {
        "uuid": str(uuid.uuid4()),
        "number": "SCRW-2003",
        "name": "Screw ISO 4762 M6x35",
        "description": "A hexagon socket head cap screw for fastening metal parts",
        "revision": "1",
        "lifecycle_state": "In Work",
        "owner": "Max Mustermann",
        "material": "Steel",
        "quantity": 200,
        "cad_reference": "CAD REFERENCE CARRIAGE BOLT",
        "attached_documents_reference": "DOCUMENTS REFERENCE CARRIAGE BOLT",
        "lead_time": 5,
        "make_or_buy": "buy",
        "supplier": "Adolf Würth GmbH & Co. KG",
        "manufacturer_number": "MFN-100003",
        "unit_price": 0.25,
        "currency": "EUR"
    }
]
'''