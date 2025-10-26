# Dashboard de Análisis - Metal Veneta

## Instrucciones de Uso

### 1. Ejecutar Localmente

```bash
# Instalar dependencias
pip install -r requirements.txt

# Ejecutar el dashboard
streamlit run app/main.py
```

El dashboard se abrirá automáticamente en tu navegador en `http://localhost:8501`

### 2. Desplegar para Presentación (QR Code)

#### Opción A: Streamlit Cloud (Recomendado - Gratis)
1. Sube el proyecto a GitHub
2. Ve a [share.streamlit.io](https://share.streamlit.io)
3. Conecta tu repositorio
4. Configura el archivo a ejecutar: `app/main.py`
5. Obtén la URL pública
6. Genera un QR code con esa URL (usando [qr-code-generator.com](https://www.qr-code-generator.com))

#### Opción B: Render
1. Crea cuenta en [render.com](https://render.com)
2. Conecta tu repositorio de GitHub
3. Crea un nuevo Web Service
4. Configura:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `streamlit run app/main.py --server.port $PORT`
5. Despliega y obtén la URL

#### Opción C: Railway
1. Crea cuenta en [railway.app](https://railway.app)
2. Click "New Project" → "Deploy from GitHub"
3. Selecciona tu repositorio
4. Railway detectará automáticamente Streamlit
5. Despliega y obtén la URL

### 3. Generar QR Code

Una vez que tengas la URL pública:

```bash
# Usando Python
pip install qrcode[pil]
python -c "import qrcode; img = qrcode.make('TU_URL_AQUI'); img.save('qr_dashboard.png')"
```

O usa un generador online: [qr-code-generator.com](https://www.qr-code-generator.com)

### 4. Personalización para Presentación

Para cambiar los colores o estilos del dashboard, edita:
- `app/main.py` - Funciones `render_*` para colores específicos
- Configuración: `config/rendimiento_base.yaml`

## Uso Durante la Presentación

### Modo Proyección
1. Conecta tu laptop al proyector
2. Abre el dashboard en navegador en modo pantalla completa
3. Navega entre las pestañas según tu presentación

### Interacción del Público
1. Muestra el QR code en la pantalla
2. La audiencia escanea y accede al dashboard
3. Pueden interactuar con filtros y visualizaciones
4. Cada persona explora a su ritmo

### Tips
- **Prueba la conectividad** antes de la presentación
- Ten un **plan B**: capturas de pantalla o video grabado
- **Prueba el QR** con varios celulares diferentes
- Considera **red local** si el WiFi es problemático

## Troubleshooting

### El dashboard no carga
- Verifica que todas las dependencias estén instaladas
- Revisa que el archivo Excel esté en la ubicación correcta
- Mira los logs en la terminal

### El dashboard es lento
- Reduce la cantidad de datos mostrados
- Ajusta los filtros por defecto
- Usa un servidor más potente para producción

### Error al desplegar
- Verifica que `requirements.txt` esté actualizado
- Asegúrate de que `app/main.py` sea el punto de entrada
- Revisa los logs de despliegue en la plataforma

## Próximos Pasos

1. ✅ Dashboard funcional con visualizaciones
2. ⏳ Probar localmente
3. ⏳ Desplegar en plataforma cloud
4. ⏳ Generar QR code
5. ⏳ Probar en móvil
6. ⏳ Actualizar datos reales de Metal Veneta
7. ⏳ Preparar presentación con dashboard
