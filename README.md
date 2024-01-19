# CSV-to-SQLITE-to-PostgreSQL
 file manipulations and transfer from DB type to DB type


This is a little manual for passing the values from CSV file to SQLITE Database
and from SQLITE DB to POSTGRESQL DB.

All of this was done via Python Django features:

Create models that matches the columns header and data type you want to pass to the DB
python manage.py makemigrations
python manage.py migrate

Open the SQLITE DB with SQLITE Studio and load values of the CSV file into the table.
Handeling the value type and provide necessary steps to perform the action.

Then back to Django.

python manage.py dumpdata --output data.json

[The --output is important here, do not use > as pycharm seems to add additional lines in the JSON file]

Do the necessary changes in the settings.py to connect to the POSTGRESQL DB (created manually) 

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'djtest',
        'USER':'xxxxxxx',
        'PASSWORD':'xxxxxxx',
        'HOST':'localhost',
        'PORT':'5432',
    }
}




python manage.py migrate --run-syncdb
python manage.py loaddata data.json



CSV number format as decimal 2 digits after (.)
example of datatype in SQLITE (see picture)


