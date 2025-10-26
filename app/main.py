from __future__ import annotations

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from analysis import compute_rendimiento_scenarios
from analysis.config import load_rendimiento_config, RendimientoConfig
from data import load_materia_prima_table


def render_kpi_metrics(resultados: pd.DataFrame) -> None:
    """Render key performance indicators."""
    avg_improvement = resultados['mejora_pct'].mean() * 100
    total_delta_weight = resultados['delta_peso_salida'].sum()
    max_improvement = resultados['mejora_pct'].max() * 100
    materials_count = len(resultados)
    
    # Modern KPI cards with custom styling
    st.markdown("""
    <div style='display: flex; gap: 1rem; margin: 2rem 0;'>
        <div style='flex: 1; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                    padding: 1.5rem; border-radius: 15px; color: white; text-align: center;'>
            <h3 style='color: white; font-size: 2.5rem; margin: 0;'>{:.1f}%</h3>
            <p style='color: rgba(255,255,255,0.9); margin: 0.5rem 0 0 0;'>Mejora Promedio</p>
        </div>
        <div style='flex: 1; background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); 
                    padding: 1.5rem; border-radius: 15px; color: white; text-align: center;'>
            <h3 style='color: white; font-size: 2.5rem; margin: 0;'>{:.1f} kg</h3>
            <p style='color: rgba(255,255,255,0.9); margin: 0.5rem 0 0 0;'>Impacto en Peso</p>
        </div>
        <div style='flex: 1; background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); 
                    padding: 1.5rem; border-radius: 15px; color: white; text-align: center;'>
            <h3 style='color: white; font-size: 2.5rem; margin: 0;'>{:.1f}%</h3>
            <p style='color: rgba(255,255,255,0.9); margin: 0.5rem 0 0 0;'>Mejora Máxima</p>
        </div>
        <div style='flex: 1; background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%); 
                    padding: 1.5rem; border-radius: 15px; color: white; text-align: center;'>
            <h3 style='color: white; font-size: 2.5rem; margin: 0;'>{}</h3>
            <p style='color: rgba(255,255,255,0.9); margin: 0.5rem 0 0 0;'>Materiales Analizados</p>
        </div>
    </div>
    """.format(avg_improvement, total_delta_weight, max_improvement, materials_count), 
    unsafe_allow_html=True)


def render_rendimiento_comparison(resultados: pd.DataFrame) -> None:
    """Compare base vs new line rendimiento."""
    fig = go.Figure()
    
    # Multiplicar por 100 para mostrar como porcentaje
    rend_base_pct = resultados['rendimiento_base'] * 100
    rend_new_pct = resultados['rendimiento_nueva_linea'] * 100
    
    fig.add_trace(go.Bar(
        name='Línea Base',
        x=resultados['codigo'],
        y=rend_base_pct,
        marker_color='#1a1a1a',
        text=rend_base_pct.apply(lambda x: f'{x:.2f}%'),
        textposition='auto',
    ))
    
    fig.add_trace(go.Bar(
        name='Nueva Línea',
        x=resultados['codigo'],
        y=rend_new_pct,
        marker_color='#800020',
        text=rend_new_pct.apply(lambda x: f'{x:.2f}%'),
        textposition='auto',
    ))
    
    fig.update_layout(
        title='Comparación de Rendimiento: Base vs Nueva Línea',
        xaxis_title='Código de Material',
        yaxis_title='Rendimiento (%)',
        barmode='group',
        height=500,
        showlegend=True,
        xaxis_tickangle=-45,
        # Add animations
        updatemenus=[
            dict(
                type="buttons",
                direction="left",
                buttons=list([
                    dict(
                        args=[{"visible": [True, True]}],
                        label="Ver Todo",
                        method="restyle"
                    ),
                    dict(
                        args=[{"visible": [True, False]}],
                        label="Solo Línea Base",
                        method="restyle"
                    ),
                    dict(
                        args=[{"visible": [False, True]}],
                        label="Solo Nueva Línea",
                        method="restyle"
                    ),
                ]),
                pad={"r": 10, "t": 87},
                showactive=True,
                x=0.1,
                xanchor="left",
                y=1.1,
                yanchor="top"
            ),
        ]
    )
    
    st.plotly_chart(fig, use_container_width=True)


def render_improvement_ranking(resultados: pd.DataFrame) -> None:
    """Show top improvements."""
    # Convertir mejoras a porcentajes para la visualización
    resultados_copy = resultados.copy()
    resultados_copy['delta_rendimiento_pct_display'] = resultados_copy['delta_rendimiento_pct'] * 100
    resultados_copy['mejora_pct_display'] = resultados_copy['mejora_pct'] * 100
    
    top_materials = resultados_copy.nlargest(10, 'delta_rendimiento_pct_display')
    
    fig = px.bar(
        top_materials,
        x='delta_rendimiento_pct_display',
        y='codigo',
        orientation='h',
        text='mejora_pct_display',
        labels={'delta_rendimiento_pct_display': 'Mejora en Rendimiento (%)', 'codigo': 'Material'},
        title='Top 10 Materiales con Mayor Mejora',
        color='delta_rendimiento_pct_display',
        color_continuous_scale='Viridis',
    )
    
    fig.update_traces(texttemplate='%{text:.2f}%', textposition='outside')
    
    st.plotly_chart(fig, use_container_width=True)


def render_weight_impact(resultados: pd.DataFrame) -> None:
    """Show impact on output weight."""
    fig = make_subplots(
        rows=1, cols=2,
        subplot_titles=('Peso de Salida Base', 'Peso de Salida Nueva Línea'),
        horizontal_spacing=0.15,
    )
    
    # Base weight
    fig.add_trace(
        go.Bar(
            x=resultados['codigo'],
            y=resultados['peso_salida_base'],
            name='Base',
            marker_color='#1a1a1a',
        ),
        row=1, col=1
    )
    
    # New weight
    fig.add_trace(
        go.Bar(
            x=resultados['codigo'],
            y=resultados['peso_salida_nueva_linea'],
            name='Nueva Línea',
            marker_color='#800020',
        ),
        row=1, col=2
    )
    
    fig.update_xaxes(tickangle=-45, row=1, col=1)
    fig.update_xaxes(tickangle=-45, row=1, col=2)
    fig.update_yaxes(title_text='Peso (kg)', row=1, col=1)
    fig.update_yaxes(title_text='Peso (kg)', row=1, col=2)
    fig.update_layout(height=500, showlegend=False)
    
    st.plotly_chart(fig, use_container_width=True)


def render_classification_comparison(resultados: pd.DataFrame) -> None:
    """Compare improvements by classification."""
    by_clasification = resultados.groupby('clasificacion').agg({
        'delta_rendimiento_pct': 'mean',
        'delta_peso_salida': 'sum',
    }).reset_index()
    
    # Convertir a porcentaje para visualización
    by_clasification['delta_rendimiento_pct_display'] = by_clasification['delta_rendimiento_pct'] * 100
    
    fig = px.bar(
        by_clasification,
        x='clasificacion',
        y='delta_rendimiento_pct_display',
        title='Mejora Promedio por Clasificación',
        labels={'delta_rendimiento_pct_display': 'Mejora Promedio (%)', 'clasificacion': 'Clasificación'},
        color='delta_rendimiento_pct_display',
        color_continuous_scale='Plasma',
        text=by_clasification['delta_rendimiento_pct_display'].apply(lambda x: f'{x:.2f}%'),
    )
    
    fig.update_traces(textposition='outside')
    
    st.plotly_chart(fig, use_container_width=True)


def render_waterfall(resultados: pd.DataFrame) -> None:
    """Show waterfall chart of improvements."""
    total_base = resultados['peso_salida_base'].sum()
    total_new = resultados['peso_salida_nueva_linea'].sum()
    total_delta = total_new - total_base
    
    fig = go.Figure(go.Waterfall(
        name="Impacto Total",
        orientation="v",
        measure=["absolute", "relative", "absolute"],
        x=["Peso Salida Base", "Mejora Nueva Línea", "Peso Salida Nueva"],
        textposition="outside",
        text=[f"{total_base:.1f} kg", f"+{total_delta:.1f} kg", f"{total_new:.1f} kg"],
        y=[total_base, total_delta, total_new],
        connector={"line": {"color": "rgb(63, 63, 63)"}},
    ))
    
    fig.update_layout(
        title="Análisis de Flujo: Impacto Total de la Nueva Línea",
        showlegend=False,
        height=400,
    )
    
    st.plotly_chart(fig, use_container_width=True)


def main() -> None:
    st.set_page_config(
        page_title="Metal Veneta · Análisis Pretratamiento",
        layout="wide",
        page_icon="📊",
        initial_sidebar_state="expanded",
    )
    
    # Custom CSS for modern design with animations
    st.markdown("""
    <style>
    /* Main styling - white background */
    .main > div {
        padding-top: 2rem;
    }
    .stApp {
        background-color: white;
    }
    /* Smooth transitions for buttons and elements */
    button, select, input {
        transition: all 0.3s ease;
    }
    button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
    /* Animate KPIs on load */
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    /* Smooth fade in for content */
    .element-container {
        animation: fadeInUp 0.6s ease-out;
    }
    h1 {
        color: #1a1a1a;
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    h2 {
        color: #1a1a1a;
        font-size: 1.5rem;
        font-weight: 600;
    }
    h3 {
        color: #1a1a1a;
        font-size: 1.25rem;
        font-weight: 600;
    }
    /* All text should be dark on white background */
    p, div, span {
        color: #1a1a1a;
    }
    /* Metric cards */
    [data-testid="stMetricValue"] {
        font-size: 2rem;
        font-weight: 700;
    }
    [data-testid="stMetricDelta"] {
        font-size: 1rem;
    }
    /* Sidebar */
    .css-1d391kg {
        padding-top: 2rem;
    }
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)
    
    # Header with Metal Veneta colors (black, white, burgundy)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
        <div style='text-align: center; padding: 2rem 0; background: linear-gradient(135deg, #1a1a1a 0%, #800020 100%); 
                    border-radius: 15px; margin-bottom: 2rem; border: 3px solid #800020;'>
            <h1 style='color: white; margin: 0; padding: 0.5rem 0; font-weight: bold;'>Metal Veneta</h1>
            <p style='color: #fff; font-size: 1.2rem; margin: 0; opacity: 0.95;'>Análisis de Línea de Pretratamiento</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Load data
    with st.spinner("Cargando datos..."):
        config = load_rendimiento_config()
        dataset = load_materia_prima_table()
        resultados = compute_rendimiento_scenarios(dataset.table, config)
    
    # Sidebar with Metal Veneta colors
    st.sidebar.markdown("""
    <div style='background: linear-gradient(135deg, #1a1a1a 0%, #800020 100%); 
                padding: 1.5rem; border-radius: 10px; margin-bottom: 2rem; border: 2px solid #800020;'>
        <h2 style='color: white; margin: 0; font-size: 1.3rem;'>📊 Filtros</h2>
        <p style='color: rgba(255,255,255,0.9); margin: 0.5rem 0 0 0; font-size: 0.9rem;'>
            Personaliza tu análisis
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Classification filter
    clasificaciones = ['Todos'] + sorted(resultados['clasificacion'].unique().tolist())
    selected_clasif = st.sidebar.selectbox("🗂️ Clasificación", clasificaciones)
    
    if selected_clasif != 'Todos':
        resultados = resultados[resultados['clasificacion'] == selected_clasif]
    
    # Format filter
    formatos = ['Todos'] + sorted(resultados['formato'].unique().tolist())
    selected_formato = st.sidebar.selectbox("📦 Formato", formatos)
    
    if selected_formato != 'Todos':
        resultados = resultados[resultados['formato'] == selected_formato]
    
    # Improvement threshold
    min_improvement = st.sidebar.slider(
        "📈 Mejora Mínima (%)",
        min_value=0.0,
        max_value=float(resultados['mejora_pct'].max() * 100),
        value=0.0,
        step=0.1,
    )
    
    resultados = resultados[resultados['mejora_pct'] * 100 >= min_improvement]
    
    # Configuration info box with Metal Veneta colors
    st.sidebar.markdown("---")
    st.sidebar.markdown("""
    <div style='background-color: #f5f5f5; padding: 1rem; border-radius: 10px; border-left: 4px solid #800020;'>
        <h4 style='color: #1a1a1a; margin: 0 0 0.5rem 0;'>⚙️ Configuración</h4>
        <p style='color: #333; margin: 0.3rem 0; font-size: 0.9rem;'>
            <strong>Mejora por defecto:</strong> {:.1f}%
        </p>
        <p style='color: #333; margin: 0.3rem 0; font-size: 0.9rem;'>
            <strong>Materiales con override:</strong> {}
        </p>
        <p style='color: #333; margin: 0.3rem 0; font-size: 0.9rem;'>
            <strong>Total de materiales:</strong> {}
        </p>
    </div>
    """.format(config.default_delta_pct * 100, len(config.overrides_pct), len(dataset.table)), 
    unsafe_allow_html=True)
    
    # Main content
    if len(resultados) == 0:
        st.warning("No hay materiales que cumplan con los filtros seleccionados.")
        return
    
    # KPIs
    render_kpi_metrics(resultados)
    st.markdown("---")
    
    # Tabs for different visualizations
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📊 Comparación Rendimiento",
        "🏆 Ranking de Mejoras",
        "⚖️ Impacto en Peso",
        "📈 Por Clasificación",
        "🌊 Análisis de Flujo"
    ])
    
    with tab1:
        st.markdown("### Comparación Directa: Rendimiento Base vs Nueva Línea")
        render_rendimiento_comparison(resultados)
    
    with tab2:
        st.markdown("### Materiales con Mayor Mejora en Rendimiento")
        render_improvement_ranking(resultados)
    
    with tab3:
        st.markdown("### Impacto en Peso de Salida")
        render_weight_impact(resultados)
        st.markdown("---")
        st.markdown("#### Distribución de Mejoras en Peso")
        # Delta distribution
        fig = px.histogram(
            resultados,
            x='delta_peso_salida',
            nbins=20,
            title='Distribución de Mejoras en Peso de Salida',
            labels={'delta_peso_salida': 'Mejora en Peso (kg)', 'count': 'Frecuencia'},
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with tab4:
        st.markdown("### Análisis por Tipo de Clasificación")
        render_classification_comparison(resultados)
        
        # Summary table by classification
        st.markdown("#### Resumen por Clasificación")
        summary = resultados.groupby('clasificacion').agg({
            'codigo': 'count',
            'mejora_pct': 'mean',
            'delta_peso_salida': 'sum',
        }).round(3)
        summary.columns = ['Cantidad Materiales', 'Mejora Promedio', 'Total Mejora Peso (kg)']
        st.dataframe(summary, use_container_width=True)
    
    with tab5:
        st.markdown("### Análisis de Flujo de Peso")
        render_waterfall(resultados)
        
        # Detailed table
        st.markdown("### Tabla Detallada de Resultados")
        display_cols = [
            'codigo', 'nombre', 'clasificacion', 'formato',
            'rendimiento_base', 'rendimiento_nueva_linea',
            'peso_salida_base', 'peso_salida_nueva_linea',
            'delta_peso_salida', 'mejora_pct'
        ]
        st.dataframe(
            resultados[display_cols],
            use_container_width=True,
            column_config={
                'rendimiento_base': st.column_config.NumberColumn('Rend. Base', format='%.3f'),
                'rendimiento_nueva_linea': st.column_config.NumberColumn('Rend. Nueva', format='%.3f'),
                'peso_salida_base': st.column_config.NumberColumn('Peso Base (kg)', format='%.1f'),
                'peso_salida_nueva_linea': st.column_config.NumberColumn('Peso Nueva (kg)', format='%.1f'),
                'delta_peso_salida': st.column_config.NumberColumn('Δ Peso (kg)', format='%.1f'),
                'mejora_pct': st.column_config.NumberColumn('Mejora %', format='%.1%'),
            }
        )
    
    # Footer with Metal Veneta colors
    st.markdown("---")
    st.markdown("""
    <div style='background: linear-gradient(135deg, #1a1a1a 0%, #800020 100%); 
                padding: 1.5rem; border-radius: 10px; margin-top: 3rem; text-align: center; border: 2px solid #800020;'>
        <p style='color: white; margin: 0; font-size: 0.95rem;'>
            📝 Los valores mostrados son proyecciones basadas en supuestos hipotéticos. 
            Se actualizarán con datos reales una vez disponible la información de Metal Veneta.
        </p>
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()

