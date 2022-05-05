init_app:
	python -m pip install -U pip
	pip install -r ../requirements.txt
	python ./manage.py migrate
	python ./manage.py loaddata backend/fixtures

run_migrations:
	python ./manage.py makemigrations
	python ./manage.py migrate

reset_db:
	find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
	find . -path "*/migrations/*.pyc"  -delete
	make run_migrations

reset_sqlite:
	rm db.sqlite3
	make reset_db