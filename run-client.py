import requests

BASE_URL = "http://localhost:5000"
if __name__ == '__main__':
    print("Starting OpenPartsLibrary Flask Client")

    response = requests.get(f"{BASE_URL}/api/read-all-parts")
    print("All parts response:", response.json())

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
        "make_or_buy": "Make",
        "supplier": "ABC Supplies",
        "manufacturer_number": "M12345",
        "unit_price": 12.5,
        "currency": "USD"
    }
    create_response = requests.post(f"{BASE_URL}/api/create-part", json=new_part)
    print("Create part response:", create_response.json())

    response = requests.get(f"{BASE_URL}/api/read-part/P12345")
    print("Single part:", response.json())
    
    update = {"quantity": 10}
    update_response = requests.put(f"{BASE_URL}/api/update-part/P12345", json=update)
    print("Update part response:", update_response.json())

    delete_response = requests.delete(f"{BASE_URL}/api/delete-part/P12345")
    print("Delete part response:", delete_response.json())

    