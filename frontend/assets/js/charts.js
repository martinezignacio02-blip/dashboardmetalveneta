// Módulo para manejar los gráficos con Chart.js

let rendimientoChart = null;

// Función para crear el gráfico de comparación de rendimientos
function createRendimientoChart(data) {
    const ctx = document.getElementById('rendimientoChart');
    
    if (!ctx) return;
    
    // Destruir gráfico existente si existe
    if (rendimientoChart) {
        rendimientoChart.destroy();
    }
    
    // Preparar datos
    const materiales = data.map(d => d.nombre || d.codigo);
    const rendimientoBase = data.map(d => d.rendimiento_base * 100);
    const rendimientoNueva = data.map(d => d.rendimiento_nueva_linea * 100);
    
    // Crear gráfico
    rendimientoChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: materiales,
            datasets: [
                {
                    label: 'Rendimiento Base (%)',
                    data: rendimientoBase,
                    backgroundColor: 'rgba(26, 26, 26, 0.8)', // Negro
                    borderColor: 'rgba(26, 26, 26, 1)',
                    borderWidth: 2
                },
                {
                    label: 'Rendimiento Nueva Línea (%)',
                    data: rendimientoNueva,
                    backgroundColor: 'rgba(128, 0, 32, 0.8)', // Bordo
                    borderColor: 'rgba(128, 0, 32, 1)',
                    borderWidth: 2
                }
            ]
        },
        options: {
            responsive: true,
            maintainAspectRatio: true,
            aspectRatio: 2,
            plugins: {
                title: {
                    display: true,
                    text: 'Comparación de Rendimientos',
                    font: {
                        size: 18,
                        weight: 'bold'
                    },
                    color: '#1a1a1a'
                },
                legend: {
                    position: 'top',
                    labels: {
                        font: {
                            size: 12
                        },
                        usePointStyle: true
                    }
                },
                tooltip: {
                    callbacks: {
                        label: function(context) {
                            return context.dataset.label + ': ' + context.parsed.y.toFixed(2) + '%';
                        }
                    }
                }
            },
            scales: {
                y: {
                    beginAtZero: true,
                    title: {
                        display: true,
                        text: 'Rendimiento (%)',
                        font: {
                            size: 14,
                            weight: 'bold'
                        }
                    },
                    ticks: {
                        callback: function(value) {
                            return value + '%';
                        }
                    }
                },
                x: {
                    title: {
                        display: true,
                        text: 'Material',
                        font: {
                            size: 14,
                            weight: 'bold'
                        }
                    },
                    ticks: {
                        maxRotation: 45,
                        minRotation: 45
                    }
                }
            }
        }
    });
}

// Función para actualizar el gráfico con filtros
function updateRendimientoChart(filteredData) {
    if (rendimientoChart) {
        // Actualizar datos
        const materiales = filteredData.map(d => d.nombre || d.codigo);
        const rendimientoBase = filteredData.map(d => d.rendimiento_base * 100);
        const rendimientoNueva = filteredData.map(d => d.rendimiento_nueva_linea * 100);
        
        rendimientoChart.data.labels = materiales;
        rendimientoChart.data.datasets[0].data = rendimientoBase;
        rendimientoChart.data.datasets[1].data = rendimientoNueva;
        
        rendimientoChart.update('active');
    }
}

// Exportar funciones
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        createRendimientoChart,
        updateRendimientoChart
    };
}
