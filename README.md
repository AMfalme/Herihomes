Local Setup
To run locally:

create a python3 virtual environment
pip install -r requirements.txt
./manage.py collectstatic
./manage.py makemigrations
./manage.py migrate
./manage.py createsuperuser
./manage.py runserver
go to the admin site and create the first page/populate the information