FROM python:3.9-slim
WORKDIR /app
RUN pip install flask flask-cors mysql-connector-python
COPY . .
CMD ["python", "app.py"]
