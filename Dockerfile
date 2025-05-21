# Gunakan Python image
FROM python:3.10-slim

# Set direktori kerja di dalam container
WORKDIR /app

# Salin file aplikasi ke dalam container
COPY . /app

# Install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Jalankan Flask
CMD ["python", "app.py"]
