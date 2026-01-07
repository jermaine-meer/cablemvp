FROM python:3.11-slim
WORKDIR /app

# Installeer build-tools, libpq (voor psycopg2) en curl/ca-certificates (voor healthcheck)
RUN apt-get update && \
    apt-get install -y build-essential libpq-dev curl ca-certificates --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

# Kopieer requirements en installeer Python packages
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Kopieer rest van de app
COPY . /app

# Start Gunicorn (2 workers - goed voor ontwikkel/kleine test)
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:app", "--workers", "2", "--timeout", "120"]
