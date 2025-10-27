// Gráfico de abundancia de elementos en la corteza terrestre
document.addEventListener('DOMContentLoaded', function() {
    const ctx = document.getElementById('abundanceChart');
    const chartContainer = document.getElementById('chart-container');
    
    if (!ctx || !chartContainer) return;
    
    // Registrar el plugin de datalabels
    if (Chart && Chart.register) {
        Chart.register(ChartDataLabels);
    }
    
    let chart = null;
    let hasLoaded = false;
    
    // Función para crear el gráfico
    function createChart() {
        if (hasLoaded) return;
        
        // Datos de abundancia de elementos en la corteza terrestre (% en peso)
        chart = new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: ['Oxígeno', 'Silicio', 'Aluminio', 'Hierro', 'Calcio', 'Sodio', 'Otros'],
            datasets: [{
                offset: [0, 0, 15, 0, 0, 0, 0], // Separar aluminio hacia afuera
                data: [46.1, 28.2, 8.23, 5.63, 4.15, 2.36, 5.33], // Los últimos elementos agrupados
                backgroundColor: [
                    'rgba(121, 5, 5, 0.6)',
                    'rgba(150, 50, 50, 0.7)',
                    'rgba(200, 0, 0, 1)', // Rojo destacado para aluminio
                    'rgba(121, 5, 5, 0.5)',
                    'rgba(121, 5, 5, 0.4)',
                    'rgba(121, 5, 5, 0.35)',
                    'rgba(121, 5, 5, 0.25)'
                ],
                borderColor: [
                    'rgba(121, 5, 5, 1)',
                    'rgba(150, 50, 50, 1)',
                    'rgba(255, 0, 0, 1)', // Borde rojo brillante para aluminio
                    'rgba(121, 5, 5, 0.8)',
                    'rgba(121, 5, 5, 0.7)',
                    'rgba(121, 5, 5, 0.6)',
                    'rgba(121, 5, 5, 0.5)'
                ],
                borderWidth: [2, 2, 8, 2, 2, 2, 2], // Borde más grueso para aluminio
                borderAlign: 'center'
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            layout: {
                padding: 40
            },
            plugins: {
                legend: {
                    display: false
                },
                datalabels: {
                    display: true,
                    color: function(context) {
                        // Aluminio en rojo, el resto en blanco
                        return context.dataIndex === 2 ? '#ff0000' : '#ffffff';
                    },
                    font: function(context) {
                        return {
                            family: 'Montserrat',
                            size: context.dataIndex === 2 ? 15 : 14,
                            weight: context.dataIndex === 2 ? '900' : '600'
                        };
                    },
                    formatter: function(value, context) {
                        return context.chart.data.labels[context.dataIndex];
                    },
                    anchor: 'end',
                    align: 'end',
                    offset: 15
                },
                tooltip: {
                    backgroundColor: 'rgba(0, 0, 0, 0.8)',
                    titleColor: '#ffffff',
                    bodyColor: '#ffffff',
                    borderColor: 'rgba(121, 5, 5, 1)',
                    borderWidth: 1,
                    padding: 12,
                    callbacks: {
                        label: function(context) {
                            return context.label + ': ' + context.parsed.toFixed(1) + '%';
                        }
                    }
                }
            },
            animation: {
                duration: 2000,
                easing: 'easeOutQuart'
            },
            onClick: (event, activeElements) => {
                if (activeElements.length > 0) {
                    const index = activeElements[0].index;
                    console.log('Elemento clickeado:', chart.data.labels[index]);
                }
            }
        }
    });
    
    hasLoaded = true;
    }
    
    // Observer para detectar cuando el contenedor del gráfico entra en vista
    const observerOptions = {
        threshold: 0.3,
        rootMargin: '0px'
    };
    
    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting && !hasLoaded) {
                // Crear el gráfico cuando entra en vista
                createChart();
            }
        });
    }, observerOptions);
    
    // Observar el contenedor del gráfico
    observer.observe(chartContainer);
});
