
## Local install
* Create a new virtualenv
* Inside the virtualenv, run following commands in order to run the project
```sh
# install required modules
pip install -r requirements.txt
# add models to local database
python manage.py migrate
# create super user:
python manage.py createsuperuser
# run project
python manage.py runserver
```
## Examples
You can see a simple REST Framework usage example in this project, using `Currency` Model, Serializer and View, also added to project url, visible in `{{project_url}}/indicator/currency`, you can add fields in django admin in the url `{{project_url}}/admin`, where `project_url` commonly is: http://localhost:8000
