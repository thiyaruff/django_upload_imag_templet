# Create  a Virtual environment

pip install virtualenv (once per computer)
python -m virtualenv myenv (once per project)
myenv\Scripts\activate  (Activate)

# to run the project

py manage.py runserver

# Migration -create the tables
python manage.py makemigrations
py manage.py migrate 

# creat superuser

allready exist: 
UserName:thiya
password:123

# or 

py manage.py createsuperuser

# to check in the admin

http://127.0.0.1:8000/admin
