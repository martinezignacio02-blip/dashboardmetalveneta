// Configuración de la API
// const API_URL = 'http://localhost:8000';  // Local
const API_URL = 'https://metal-veneta-api.onrender.com';  // Producción

// Función para obtener el resumen de datos
async function getResumen() {
    try {
        const response = await fetch(`${API_URL}/api/rendimientos/resumen`);
        const data = await response.json();
        
        if (data.success) {
            return data.data;
        } else {
            throw new Error(data.error || 'Error al cargar los datos');
        }
    } catch (error) {
        console.error('Error fetching resumen:', error);
        throw error;
    }
}

// Función para obtener todos los datos de rendimientos
async function getRendimientos() {
    try {
        const response = await fetch(`${API_URL}/api/rendimientos`);
        const data = await response.json();
        
        if (data.success) {
            return data.data;
        } else {
            throw new Error(data.error || 'Error al cargar los datos');
        }
    } catch (error) {
        console.error('Error fetching rendimientos:', error);
        throw error;
    }
}
