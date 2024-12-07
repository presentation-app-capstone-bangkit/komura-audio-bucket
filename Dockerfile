# Gunakan Python base image
FROM python:3.9-slim

# Set working directory di dalam container
WORKDIR /app

# Install dependencies sistem termasuk FFmpeg
RUN apt-get update && apt-get install -y ffmpeg && apt-get clean

# Salin semua file dari project lokal ke container
COPY . .

# Install dependencies Python
RUN pip install --no-cache-dir -r requirements.txt

# Expose port Flask
EXPOSE 8080

# Jalankan aplikasi
CMD ["python", "app.py"]
