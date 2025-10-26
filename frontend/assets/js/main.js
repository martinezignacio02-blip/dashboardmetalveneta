// Función para crear una tarjeta KPI
function createKPICard(label, value, unit = '') {
    return `
        <div class="kpi-card">
            <div class="kpi-value">${value}${unit}</div>
            <div class="kpi-label">${label}</div>
        </div>
    `;
}

// Función para renderizar los KPIs
function renderKPIs(data) {
    const kpiContainer = document.getElementById('kpis');
    
    const kpisHTML = `
        ${createKPICard('Mejora Promedio', data.mejora_promedio.toFixed(1), '%')}
        ${createKPICard('Impacto en Peso', data.impacto_total_peso.toFixed(1), ' kg')}
        ${createKPICard('Mejora Máxima', data.mejora_maxima.toFixed(1), '%')}
        ${createKPICard('Materiales Analizados', data.total_materiales, '')}
    `;
    
    kpiContainer.innerHTML = kpisHTML;
}

// Función principal que se ejecuta al cargar la página
async function init() {
    try {
        // Obtener datos del resumen
        const resumenData = await getResumen();
        
        // Renderizar KPIs
        renderKPIs(resumenData);
        
        // Obtener todos los datos para los gráficos
        const todosLosDatos = await getRendimientos();
        
        // Crear gráfico de comparación de rendimientos
        if (typeof createRendimientoChart !== 'undefined') {
            createRendimientoChart(todosLosDatos);
        }
        
        // Ocultar el indicador de carga
        document.getElementById('loading').classList.add('hidden');
        
        console.log('Dashboard cargado exitosamente', resumenData);
    } catch (error) {
        console.error('Error inicializando dashboard:', error);
        
        // Mostrar error en la página
        const kpiContainer = document.getElementById('kpis');
        kpiContainer.innerHTML = `
            <div class="kpi-card" style="border-color: red;">
                <div class="kpi-value" style="color: red;">⚠️</div>
                <div class="kpi-label">Error al cargar los datos</div>
                <p style="font-size: 0.9rem; margin-top: 1rem; opacity: 0.8;">
                    ${error.message}
                </p>
            </div>
        `;
        
        document.getElementById('loading').classList.add('hidden');
    }
}

// Ejecutar cuando la página esté cargada
document.addEventListener('DOMContentLoaded', init);
