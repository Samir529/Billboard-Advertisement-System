# Use official Python 3.13 image
FROM python:3.13-slim

# Set environment variables
# Prevent Python from buffering stdout/stderr
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install system dependencies for common Python packages
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first (for Docker caching)
COPY requirements.txt .

# Upgrade pip and install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the rest of the application
COPY . .

# Collect static files (ensure STATIC_ROOT is set in settings.py)
RUN python manage.py collectstatic --noinput

# Expose port Render will provide
# Expose default port (optional, Render provides $PORT)
EXPOSE 8000

# Start Gunicorn server using PORT env variable provided by Render
#CMD ["gunicorn", "Billboard_Advertisement.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "4"]

# Start Gunicorn server using PORT env variable provided by Render (shell form so $PORT is expanded)
CMD gunicorn Billboard_Advertisement.wsgi:application --bind 0.0.0.0:$PORT --workers 4
