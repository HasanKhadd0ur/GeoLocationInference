def test_extract_message_location(client):
    
    response = client.post("/recognition/extract-message-location", json={"text": " تم إصدار قرار بإقالة رئيس المخفر الجنوبي في مدينة جبلة ( أبو سمير ) .. ونقله إلى منطقة أخرى"})
    assert response.status_code == 200
    data = response.get_json()
    print(data)

def test_extract_event_location(client):
    # Route: POST /extract-event-location in resolution_bp
    messages = [
        {"text": "قوات سوريا الديمقراطية تمنع بدء أعمال صيانة جسري البوكمال/ الباغوز – والعشارة درنج ، بعد وصول المعدات اللوجستية اللازمة لذلك من دون أي توضيح أو بيان رسمي .."},
        {"text": "صورة من داخل منزل في القصير بعد دخول دورية للتفتيش فيه !!"},
        {"text": "بعض الأنفاق التي حفرتها قسد بمدينة الرقة"}
    ]
    response = client.post("/recognition/extract-event-location", json=messages)
    assert response.status_code == 200
    data = response.get_json()

    assert data is not None
