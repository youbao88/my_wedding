FROM python:3.9.13-slim

WORKDIR /my_wedding_backend

RUN mkdir appData

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:80", "app:create_app()"]
