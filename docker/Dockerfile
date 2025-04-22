# Use Alpine-based Python image (0 vulnerabilities)
FROM python:3.13-alpine

# Set secure defaults (modern ENV format)
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

# Install dependencies (Alpine packages)
RUN apk add --no-cache gcc musl-dev libffi-dev

# Install Python requirements
COPY requirements.txt .
RUN apk update &&\
    pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create non-root user and set permissions
RUN adduser -D appuser && \
    chown -R appuser:appuser /app
USER appuser

# Run with Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "wsgi:app"]