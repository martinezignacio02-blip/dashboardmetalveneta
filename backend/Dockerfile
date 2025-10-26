# Dockerfile para construcción desde el directorio raíz
# Build con: docker build -f backend/Dockerfile .
FROM python:3.11-slim

WORKDIR /app

# Copiar requirements
COPY backend/requirements-api.txt ./requirements-api.txt
RUN pip install --no-cache-dir -r requirements-api.txt

# Copiar todo el código
COPY backend/api/ ./api/
COPY analysis/ ./analysis/
COPY data/ ./data/
COPY config/ ./config/

# Copiar archivo Excel desde raíz
COPY "Materia Prima Metal Veneta.xlsx" ./

EXPOSE 8000

CMD ["python", "-m", "uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
