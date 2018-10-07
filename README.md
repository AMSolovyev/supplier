# Supplier

The application displays the reference parameters of suppliers, their current price and price excess in %.
If the supplied does not have any price excess, this value is not displayed.


# Run local version
` ' #!bash

virtualenv -p python3 venv
source venv/bin/activate
pip install-r requirements.txt
python manage.py runserver
"`

Open in browser: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)