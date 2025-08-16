FROM ubuntu:latest

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Install system dependencies
RUN apt-get update && apt-get install -y \
    python3.12 \
    python3.12-dev \
    python3.12-venv \
    python3-pip \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Create a symbolic link for python
RUN ln -s /usr/bin/python3.12 /usr/bin/python

# Upgrade pip
RUN python -m pip install --upgrade pip

# Set work directory
WORKDIR /app

# Copy requirements first to leverage Docker cache
COPY requirements.txt .
COPY pyproject.toml .

# Install Python dependencies
RUN pip install -r requirements.txt
RUN pip install -e .

# Copy project
COPY . .

# Create a non-root user
RUN useradd -m -u 1000 appuser && chown -R appuser:appuser /app
USER appuser

# Command to show Python version and run the application
CMD ["sh", "-c", "echo 'Python version:' && python --version && python -m template_python_project"]
