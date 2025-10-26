# Metal Veneta - Dashboard de Análisis

Dashboard interactivo para el análisis de líneas de pretratamiento en Metal Veneta.

## 🎯 Descripción

Este proyecto analiza el impacto de una nueva línea de pretratamiento de aluminio secundario en Metal Veneta, Córdoba, Argentina.

## 🏗️ Arquitectura

- **Backend**: API REST con FastAPI (Python)
- **Frontend**: HTML/CSS/JavaScript con Chart.js
- **Datos**: Análisis de rendimientos base vs. nueva línea

## 📁 Estructura

```
├── backend/              # API y lógica de negocio
│   ├── api/              # FastAPI endpoints
│   ├── analysis/         # Cálculos de rendimientos
│   ├── data/             # Carga de datos
│   └── config/           # Configuración
├── frontend/             # Interfaz visual
│   ├── assets/           # CSS, JS, imágenes
│   └── index.html        # Página principal
└── docs/                 # Documentación
```

## 🚀 Inicio Rápido

### Local

1. **Backend**
   ```bash
   cd backend
   python api/main.py
   ```
   API disponible en: http://localhost:8000

2. **Frontend**
   - Abrir `frontend/index.html` en el navegador
   - O usar un servidor local

### Deployment

Ver [docs/DEPLOYMENT.md](docs/DEPLOYMENT.md)

## 📊 Endpoints API

- `GET /` - Estado del servidor
- `GET /api/rendimientos` - Todos los datos
- `GET /api/rendimientos/resumen` - KPIs principales

## 🛠️ Tecnologías

- Python 3.11
- FastAPI
- Pandas
- Chart.js
- JavaScript ES6+

## 📝 Documentación

- [Arquitectura Híbrida](docs/ARQUITECTURA_HIBRIDA.md)
- [Guía de Deployment](docs/DEPLOYMENT.md)
- [Estado del Proyecto](docs/PROYECTO_STATUS.md)

## 👥 Autores

Estudiantes de Ingeniería Industrial - Universidad Católica de Córdoba

## 📄 Licencia

Proyecto académico - Metal Veneta 2024
