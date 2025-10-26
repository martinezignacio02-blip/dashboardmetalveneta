"""API Backend para el Dashboard de Metal Veneta"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
import sys

# Agregar el directorio raíz al path para importar los módulos existentes
sys.path.append(str(Path(__file__).parent.parent.parent))

from analysis import compute_rendimiento_scenarios
from analysis.config import load_rendimiento_config
from data import load_materia_prima_table

# Crear la aplicación FastAPI
app = FastAPI(
    title="Metal Veneta Dashboard API",
    description="API para el análisis de líneas de pretratamiento",
    version="1.0.0"
)

# Configurar CORS para permitir requests desde el frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción, cambiar a la URL específica del frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    """Endpoint de prueba"""
    return {"message": "API Metal Veneta Dashboard", "status": "running"}


@app.get("/api/rendimientos")
def get_rendimientos():
    """
    Obtiene todos los datos de rendimientos calculados
    Retorna un JSON con los resultados del análisis
    """
    try:
        # Cargar datos y calcular escenarios
        dataset = load_materia_prima_table()
        config = load_rendimiento_config()
        resultados = compute_rendimiento_scenarios(dataset.table, config)
        
        # Convertir a diccionario para JSON
        return {
            "success": True,
            "data": resultados.to_dict(orient="records")
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }


@app.get("/api/rendimientos/resumen")
def get_resumen():
    """
    Obtiene un resumen de los KPIs principales
    """
    try:
        dataset = load_materia_prima_table()
        config = load_rendimiento_config()
        resultados = compute_rendimiento_scenarios(dataset.table, config)
        
        return {
            "success": True,
            "data": {
                "total_materiales": len(resultados),
                "mejora_promedio": float(resultados['mejora_pct'].mean() * 100),
                "mejora_maxima": float(resultados['mejora_pct'].max() * 100),
                "impacto_total_peso": float(resultados['delta_peso_salida'].sum()),
                "clasificaciones": resultados['clasificacion'].unique().tolist(),
                "formatos": resultados['formato'].unique().tolist(),
            }
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }


if __name__ == "__main__":
    import uvicorn
    import os
    
    # Render usa la variable de entorno PORT
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
