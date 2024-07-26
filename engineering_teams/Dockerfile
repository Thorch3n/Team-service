FROM python:3.9

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /app

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "engineering_teams.wsgi:application"]
