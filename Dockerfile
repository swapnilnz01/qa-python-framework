FROM jenkins/jenkins:lts

USER root

# install python and system dependencies
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    libnss3 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libcups2 \
    libdrm2 \
    libxkbcommon0 \
    libxcomposite1 \
    libxdamage1 \
    libxfixes3 \
    libxrandr2 \
    libgbm1 \
    libasound2 \
    libpango-1.0-0 \
    libpangocairo-1.0-0 \
    && rm -rf /var/lib/apt/lists/*

# install playwright and chromium as root so all users can access it
RUN pip3 install playwright --break-system-packages \
    && playwright install chromium \
    && chmod -R 777 /root/.cache/ms-playwright

USER jenkins