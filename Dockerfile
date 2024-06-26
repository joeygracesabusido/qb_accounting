FROM python:3.10

WORKDIR /code

COPY ./requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY ./apps ./apps

CMD ["uvicorn", "apps.main:app", "--host", "0.0.0.0", "--port", "80"]
