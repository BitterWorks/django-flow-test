# Dev
dev:
	uvicorn project.asgi:application --reload --host 0.0.0.0 --port 8000

migrate:
	python manage.py migrate

dump:
	python manage.py dumpdata > data.json

load:
	python manage.py loaddata data.json

reset_db:
	python manage.py reset_db --noinput
