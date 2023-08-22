python3 -m venv /opt/render/project/src/venv

/opt/render/project/src/.venv/bin/python -m pip install --upgrade pip
pip install gunicorn
pip install rpds-py
pip install -r requirementsVercel.txt

source /opt/render/project/src/venv/bin/activate
python manage.py collectstatic --noinput