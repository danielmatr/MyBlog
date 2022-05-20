run:
	python manage.py runserver

migrate:
	./manage.py makemigrations
	./manage.py migrate
git push:
	git add .
	git commit -m 'immediately push'
	git push origin master 
