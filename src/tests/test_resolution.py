def test_geocode(client):
    response = client.post("/resolution/geocode", json={"text": "Aleppo"})
    assert response.status_code == 200
    data = response.get_json()
    assert "latitude" in data and "longitude" in data

def test_common_location(client):
    texts = ["Explosion in Damascus", "Clashes in Damascus", "Fire in Damascus"]
    response = client.post("/resolution/common-location", json={"texts": texts})
    assert response.status_code == 200
    data = response.get_json()
    assert data.get("common_location") == "Damascus"
