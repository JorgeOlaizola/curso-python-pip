FROM python:3.8

WORKDIR /csv_app
COPY requirements.txt /csv_app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /csv_app/requirements.txt

COPY . /csv_app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"] 