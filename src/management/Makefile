init_app:
	python -m pip install -U pip
	pip install -r ../requirements.txt
	python ./manage.py migrate
	python ./manage.py loaddata backend/fixtures

run_migrations:
	python ./manage.py makemigrations
	python ./manage.py migrate