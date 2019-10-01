# Installations and Configuration for Bangazon Workforce API

1. Clone this repository to your machine
1. `cd bangazon-workforce-API`
1. `python -m venv WorkforceEnv`
1. Activate the enviroment. Use the `source ./WorkforceEnv/bin/activate` command on OSX, or run `activate.bat` for Windows.
1. `pip install -r requirements.txt`

## Create Base Django Tables

Run the migration commands to set up the initial Django tables.

```sh
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
