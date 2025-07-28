# -------- Stage 1: Build environment with dev tools --------
FROM python:3.10-slim AS builder

WORKDIR /install

# Install only what's needed to build wheels
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    build-essential \
    libmupdf-dev \
    libfreetype6-dev \
    libjpeg-dev \
    zlib1g-dev

# Install dependencies to a temporary location
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# -------- Stage 2: Clean runtime --------
FROM python:3.10-slim

WORKDIR /app

# Copy installed packages from builder
COPY --from=builder /install /usr/local

# Copy app code
COPY . .

# Remove any cache, unused files, locales
RUN apt-get purge -y --auto-remove && \
    rm -rf /var/lib/apt/lists/* /root/.cache /usr/share/doc /usr/share/locale

# Start the app
CMD ["python", "main_enhanced.py"]