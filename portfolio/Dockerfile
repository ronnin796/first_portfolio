# Use a minimal Python image
FROM python:3.11-slim

# Environment settings
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory inside container
WORKDIR /app

# Install system dependencies (for common packages like psycopg2, Pillow, etc.)
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy entire Django project into the container
COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose the port gunicorn will run on
EXPOSE 8000

# Start the application using gunicorn
CMD ["gunicorn", "portfolio.wsgi:application", "--bind", "0.0.0.0:8000"]
