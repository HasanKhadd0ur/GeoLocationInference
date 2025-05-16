
def test_extract_event_location(client):
    # Route: POST /extract-event-location in resolution_bp
    messages = [
        {"text": "Explosion in Damascus"},
        {"text": "Clashes in Aleppo"},
        {"text": "Fire in Homs"}
    ]
    response = client.post("/resolution/extract-event-location", json=messages)
    assert response.status_code == 200
    data = response.get_json()
    print(data)

    assert data is not None

def test_geocode(client):
    # route is GET /geocode with ?location= param
    response = client.get("/resolution/geocode", query_string={"location": "Aleppo"})
    assert response.status_code == 200
    data = response.get_json()
    print(data)
    assert "latitude" in data and "longitude" in data
