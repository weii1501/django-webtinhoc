python3 -m venv /opt/render/project/src/.venv
source /opt/render/project/src/.venv/bin/activate

/opt/render/project/src/.venv/bin/python -m pip install --upgrade pip
pip install gunicorn
pip install rpds-py
pip install -r requirementsVercel.txt


python manage.py collectstatic --noinput