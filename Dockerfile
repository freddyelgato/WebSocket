
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt ./
COPY server.py ./
COPY index.html ./

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000


CMD ["python", "server.py"]
