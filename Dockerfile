FROM python:3.11-slim

# Instala o navegador Chromium e o Driver
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    unzip \
    chromium \
    chromium-driver \
    --no-install-recommends && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Instala a biblioteca Selenium
RUN pip install --no-cache-dir selenium

# Copia o script para dentro do container
COPY bot.py .

# Comando para rodar o bot
CMD ["python", "bot.py"]