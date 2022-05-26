init_app:
	python -m pip install -U pip
	pip install -r ../requirements.txt
	./manage.py migrate
	./manage.py loaddata backend/fixtures

run_migrations:
	./manage.py makemigrations
	/manage.py migrate