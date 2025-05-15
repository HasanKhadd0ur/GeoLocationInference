def test_recognition_llm(client):
    response = client.post("/recognition/", json={"text": "I traveled to Aleppo and Damascus."})
    assert response.status_code == 200
    data = response.get_json()
    assert "locations" in data
    assert "Aleppo" in data["locations"]
