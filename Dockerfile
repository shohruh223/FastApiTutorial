FROM python:3.12-slim

# Env
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

# Workdir
WORKDIR /app

# Dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# App code
COPY . .

# (Optional) document the port
EXPOSE 8000

# Run FastAPI app at app/main.py -> app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]