python3 -m venv /opt/render/project/src/.venv
source /opt/render/project/src/.venv/bin/activate

/opt/render/project/src/.venv/bin/python -m pip install --upgrade pip
/opt/render/project/src/.venv/bin/python -m pip install --upgrade setuptools
/opt/render/project/src/.venv/bin/python -m pip install --upgrade wheel
pip install daphne
pip install django-allauth
pip install gunicorn
pip install rpds-py
pip install -r requirementsVercel.txt


python manage.py collectstatic --noinput