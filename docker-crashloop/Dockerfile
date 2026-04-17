FROM python:3.10-slim

workdir /app

copy requirements.txt .

run pip install --no-cache-dir -r requirements.txt

copy . .

expose 5002

cmd ["python", "app.py"]