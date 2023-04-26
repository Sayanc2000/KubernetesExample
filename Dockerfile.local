FROM python:3.9

WORKDIR /server/app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

ENTRYPOINT ["uvicorn", "app.main:app"]

CMD ["--reload", "--host", "0.0.0.0", "--port", "8000"]