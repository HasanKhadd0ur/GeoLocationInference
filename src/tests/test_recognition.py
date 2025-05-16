def test_extract_message_location(client):
    
    response = client.post("/recognition/extract-message-location", json={"text": " تم إصدار قرار بإقالة رئيس المخفر الجنوبي في مدينة جبلة ( أبو سمير ) .. ونقله إلى منطقة أخرى"})
    assert response.status_code == 200
    data = response.get_json()
    print(data)
