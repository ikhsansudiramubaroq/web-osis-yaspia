# 1. Gunakan Python versi ringan
FROM python:3.11-slim

# 2. Set variabel agar log Python langsung muncul di terminal
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 3. Tentukan folder kerja di dalam kontainer
WORKDIR /app

# 4. Instal dependensi sistem untuk Postgres & Pillow
RUN apt-get update && apt-get install -y \
    libpq-dev gcc \
    && rm -rf /var/lib/apt/lists/*

# 5. Instal library Python
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# 6. Copy semua kode project Bapak ke dalam kontainer
COPY . /app/

# 7. Jalankan Gunicorn (Server Production)
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "web_osis.wsgi:application"]