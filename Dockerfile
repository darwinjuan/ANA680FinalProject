FROM python:3.9-slim
WORKDIR /app
COPY . /app
RUN pip install --default-timeout=1000 -r requirements.txt
EXPOSE 5000
CMD ["python", "app.py"]
