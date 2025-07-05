
def test_geocode(client):
    # route is GET /geocode with ?location= param
    response = client.get("/resolution/geocode", query_string={"location": "Aleppo"})
    assert response.status_code == 200
    data = response.get_json()
    print(data)
    assert "latitude" in data and "longitude" in data
