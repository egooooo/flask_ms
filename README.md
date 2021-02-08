# FLASK MS

1. Create virtualenv and activate:
```bash
virtualenv venv_flask_ms --python=python3.8

source venv_flask_ms/bin/activate
```

2. Requirements
```bash
pip install -r requirements.txt
```

**Database**
```bash
python manage.py db init

python manage.py db migrate

python manage.py db upgrade
```

## Run backend
```bash
python manage.py run
```
