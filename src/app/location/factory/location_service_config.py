class LocationServiceConfigManager:
    _instance = None
    _recognizer_key = "ner"      # default
    _resolver_key = "nominatim"  # default

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def get_recognizer_key(self) -> str:
        return self._recognizer_key

    def set_recognizer_key(self, key: str):
        self._recognizer_key = key

    def get_resolver_key(self) -> str:
        return self._resolver_key

    def set_resolver_key(self, key: str):
        self._resolver_key = key
