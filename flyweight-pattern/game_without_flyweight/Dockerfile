FROM python:3.12-slim

WORKDIR /app
RUN pip install psutil
COPY app_with_flyweight.py .

CMD ["python", "app_with_flyweight.py"]
