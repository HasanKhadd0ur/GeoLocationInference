# SAS.LocationInferenceService

The **SAS.LocationInferenceService** is a Flask-based microservice designed to infer and resolve geographic locations from textual messages, particularly in the context of situational awareness and event detection.

## 🚀 Features

* **Message-Level Location Extraction**: Extracts one or more geographic locations mentioned in a single message.
* **Event-Level Location Inference**: Infers the most likely location of an event based on multiple related messages.
* **Geocoding**: Converts location names into coordinates using a resolver service.
* **Runtime Configuration**: Dynamically switch between different recognizer/resolver services via API.

---

## 📦 Project Structure

```
src/
│
├── app/
│   ├── location/
│   │   ├── recognizer/              # Location extraction services
│   │   ├── resolver/                # Geocoding services
│   │   └── factory/                 # Service instantiation and configuration
│
├── routes/
│   ├── recognition_routes.py       # /recognition endpoints
│   ├── resolution_routes.py        # /resolution endpoints
│   └── config_routes.py            # /config endpoints
│
└── main.py                         # Flask entrypoint
```

---

## 🧪 API Endpoints

### 🔍 Location Recognition

#### `POST /recognition/extract-message-location`

Extracts geographic locations from a single message.

**Request:**

```json
{
  "text": "Explosion near the Beirut port"
}
```

**Response:**

```json
[
  {
    "name":"Beriut"
  }
]
```

---

#### `POST /recognition/extract-event-location`

Infers a representative event location from a list of messages.

**Request:**

```json
[
  { "text": "Explosion near the Beirut port" },
  { "text": "Heavy smoke in Beirut" }
]
```

**Response:**

```json
{
  "name": "Beirut, Bwirut port",
}
```

---

### 🌍 Location Resolution

#### `GET /resolution/geocode?location=Paris`

Resolves a location name to coordinates using geocoding.

**Response:**

```json
{
  "lat": 48.8566,
  "lon": 2.3522
}
```

---

### ⚙️ Configuration

#### `PUT /config/location-services/config`

Dynamically update the recognizer/resolver backend services.

**Request:**

```json
{
  "recognizer_key": "ner",
  "resolver_key": "nominatim"
}
```

**Response:**

```json
{
  "message": "Location service configuration updated",
  "recognizer_key": "ner",
  "resolver_key": "nominatim"
}
```

---

## 🐳 Running with Docker


```bash
docker build -t sas-location-inference-service .
docker run -p 5000:5000 sas-location-inference-service
```

---

## 📥 Installation (Local)

```bash
git clone https://github.com/HasanKhadd0ur/SAS.LocationInference.git
cd sas.locationinferenceservice
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
python src/main.py
```

---

## 🧠 Authors

* **Hasan Khaddour** – [LinkedIn](https://linkedin.com/in/hasankhaddour)
