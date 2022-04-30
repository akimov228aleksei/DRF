run_server:
	python -m pip install -U pip
		pip install -r ../requirements.txt
			python ./manage.py migrate
				python ./manage.py loaddata backend/fixtures
					python ./manage.py runserver

run_migration:
	python ./manage.py makemigrations
		python ./manage.py migrate

reset_db:
	find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
		find . -path "*/migrations/*.pyc"  -delete
			python ./manage.py makemigrations
				python ./manage.py migrate

reset_sqlite:
	find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
		find . -path "*/migrations/*.pyc"  -delete
			rm db.sqlite3
				python ./manage.py makemigrations
					python ./manage.py migrate