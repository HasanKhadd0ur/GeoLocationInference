from app.location.recognition.ner_recognition_service import NERLocationRecognitionService
from app.core.configs.env_config import EnvConfig

def test_extract_message_location_from_text():
    service = NERLocationRecognitionService(EnvConfig())
    result = service.extract_message_location("اجتمعوا في بيروت لإجراء المفاوضات")
    assert isinstance(result, str)
    result = result.split(',')
    assert len(result) >= 1
    assert "بيروت" in result[0]

def test_extract_event_location_multiple_messages():
    service = NERLocationRecognitionService(EnvConfig())
    messages = [
        {"text": "حدث انفجار في دمشق"},
        {"content": "الجيش ينتشر في حلب"}
    ]
    result = service.extract_event_location(messages)
    assert isinstance(result, str)
    assert any(loc in result.split(',') for loc in ["دمشق", "حلب"])
