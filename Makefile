VENV_DIR := env
PYTHON := $(VENV_DIR)/bin/python
PIP := $(VENV_DIR)/bin/pip

# Create virtual environment
venv:
	python -m venv $(VENV_DIR)

# Install dependencies
install: venv
	$(PIP) install -r requirements.txt
	$(PYTHON) -m spacy download en_core_web_sm

activate:
	$(VENV_DIR)\Scripts\activate
	
# Run the Flask app
run: activate

	PYTHON .\src\app\main.py
test:
	pytest ./src
# Install and run
dev: venv run
