import requests

BASE_URL = "http://localhost:5000"

def safe_json(response):
    try:
        return response.json()
    except Exception:
        print(response.text)
        return None
   
if __name__ == '__main__':
    print("Starting OpenPartsLibrary Flask Client")

#Adding sample parts
sample_parts = [
    {
            "number": "SCRW - 2001",
            "name": "Screw Type Z (Special) M5x14",
            "description": "A special kind of screw for safety switches",
            "revision": "1",
            "lifecycle_state": "In Work",
            "owner": "Max Mustermann",
            "material": "Steel",
            "mass": 0.03,
            "dimension_x": 0.02,
            "dimension_y": 0.005,
            "dimension_z": 0.005,
            "quantity": 100,
            "cad_reference": "CAD REFERENCE",
            "attached_documents_reference": "DOCUMENTS REFERENCE",
            "lead_time": 10,
            "make_or_buy": "make",
            "supplier": "In-House Manufacturing",
            "manufacturer_number": "MFN-100001",
            "unit_price": 0.45,
            "currency": "EUR"
        },
        {
            "number": "BOLT-2002",
            "name": "Hex Bolt",
            "description": "A standard hex bolt",
            "revision": "1",
            "lifecycle_state": "In Work",
            "owner": "Portland Bolt",
            "material": "Stainless Steel",
            "mass": 0.05,
            "dimension_x": 0.03,
            "dimension_y": 0.01,
            "dimension_z": 0.01,
            "quantity": 150,
            "cad_reference": "CAD REFERENCE BOLT",
            "attached_documents_reference": "DOCUMENTS REFERENCE BOLT",
            "lead_time": 7,
            "make_or_buy": "buy",
            "supplier": "Portland Bolt",
            "manufacturer_number": "PB-2002",
            "unit_price": 0.75,
            "currency": "EUR"
        },
        {
            "number": "BOLT-2003",
            "name": "Carriage Bolt",
            "description": "A standard carriage bolt",
            "revision": "1",
            "lifecycle_state": "In Work",
            "owner": "Fastenal",
            "material": "Carbon Steel",
            "mass": 0.04,
            "dimension_x": 0.025,
            "dimension_y": 0.008,
            "dimension_z": 0.008,
            "quantity": 200,
            "cad_reference": "CAD REFERENCE CARRIAGE BOLT",
            "attached_documents_reference": "DOCUMENTS REFERENCE CARRIAGE BOLT",
            "lead_time": 5,
            "make_or_buy": "buy",
            "supplier": "Fastenal",
            "manufacturer_number": "FB-3003",
            "unit_price": 0.60,
            "currency": "EUR"
        },
        {
            "number": "NUT-2004",
            "name": "Hex Nut",
            "description": "A standard hex nut",
            "revision": "1",
            "lifecycle_state": "In Work",
            "owner": "Grainger",
            "material": "Brass",
            "mass": 0.02,
            "dimension_x": 0.015,
            "dimension_y": 0.007,
            "dimension_z": 0.007,
            "quantity": 300,
            "cad_reference": "CAD REFERENCE HEX NUT",
            "attached_documents_reference": "DOCUMENTS REFERENCE HEX NUT",
            "lead_time": 4,
            "make_or_buy": "buy",
            "supplier": "Grainger",
            "manufacturer_number": "GN-4004",
            "unit_price": 0.30,
            "currency": "EUR"
        }
    ]

for idx, part in enumerate(sample_parts):
    create_response = requests.post(f"{BASE_URL}/api/create-part", json=part)
    result = safe_json(create_response)
    print(f"Create Part {idx + 1} Response:", result)
    if create_response.status_code != 201:
        print("Failed to create part:")
        break

    new_part = {
         "number": "P12345",
        "name": "Test Part",
        "description": "This is a test part",
        "revision": "A",
        "lifecycle_state": "In Design",
        "owner": "John Doe",
        "material": "Aluminum",
        "mass": 1.5,
        "dimension_x": 10.0,
        "dimension_y": 5.0,
        "dimension_z": 2.0,
        "quantity": 100,
        "cad_reference": "http://example.com/cad/P12345",
        "attached_documents_reference": "http://example.com/docs/P12345",
        "lead_time": 14,
        "make_or_buy": "make",
        "supplier": "ABC Supplies",
        "manufacturer_number": "M12345",
        "unit_price": 12.5,
        "currency": "USD"
    }
    create_response = requests.post(f"{BASE_URL}/api/create-part", json=new_part)
    result = safe_json(create_response)
    print("Create Part Response:", result)
    if create_response.status_code != 201:
        print("Failed to create part:")
        exit(1)

    response = requests.get(f"{BASE_URL}/api/read-all-parts")
    print("All Parts:", safe_json(response))

    response = requests.get(f"{BASE_URL}/api/read-part/P12345")
    print("Read Part Response:", safe_json(response))

    update = {"quantity": 150, "unit_price": 11.0}
    update_response = requests.put(f"{BASE_URL}/api/update-part/P12345", json=update)
    print("Update Part Response:", safe_json(update_response))

    delete_response = requests.delete(f"{BASE_URL}/api/delete-part/P12345")
    print("Delete Part Response:", safe_json(delete_response))
        