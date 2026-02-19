# 1. Bazowy obraz z Pythonem
FROM python:3.11-slim

# 2. Ustaw zmienne środowiskowe
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 3. Instalacja zależności systemowych (Chrome, ChromeDriver)
RUN apt-get update && apt-get install -y \
    wget \
    curl \
    unzip \
    chromium \
    chromium-driver \
    && rm -rf /var/lib/apt/lists/*

# 4. Ustaw katalog roboczy
WORKDIR /app

# 5. Skopiuj pliki aplikacji
COPY . /app

# 6. Instalacja zależności Pythona
RUN pip install --no-cache-dir selenium requests pycparser

# 7. Komenda startowa
CMD ["python", "Main.py"]