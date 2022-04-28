#requirements
cd src
python -m pip install -U pip
pip install -r requirements.txt

#migrations
cd management
python manage.py migrate

#fixtures 
python manage.py loaddata backend/fixtures
