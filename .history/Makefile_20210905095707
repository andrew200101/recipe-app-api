test: 
	docker-compose run app sh -c "python manage.py test && flake8"

build:
	docker-compose build

app:
	docker-compose run app sh -c "python manage.py startapp $(name)"

migrate:
	docker-compose run app sh -c "python manage.py makemigrations $(name)"

run:
	docker-compose run app sh -c "python manage.py makemigrations $(name)"