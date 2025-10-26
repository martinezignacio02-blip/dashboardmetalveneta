# Guía de Deployment - Dashboard Metal Veneta

## 🚀 Pasos para Subir a Internet

### Opción 1: Render (Recomendado - Gratis y Fácil)

#### Backend (API)

1. **Crear cuenta en Render**
   - Ve a https://render.com
   - Sign up con GitHub

2. **Subir proyecto a GitHub**
   ```bash
   cd "/Users/ignaciomartinez/Desktop/TESIS ANALISIS"
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin URL_DE_TU_REPO_GITHUB
   git push -u origin main
   ```

3. **Crear Web Service en Render**
   - Click en "New" → "Web Service"
   - Conecta tu repositorio de GitHub
   - Selecciona la rama `main`
   
   **Configuración:**
   ```
   Name: metal-veneta-api
   Environment: Python 3
   Build Command: pip install -r backend/requirements-api.txt
   Start Command: cd backend && python api/main.py
   Plan: Free
   ```

4. **Variables de Entorno**
   - Click en "Environment"
   - No necesitas variables para este proyecto

5. **¡Listo!** Render te dará una URL como:
   ```
   https://metal-veneta-api.onrender.com
   ```

#### Frontend (HTML/JS)

1. **Crear Static Site en Render**
   - Click en "New" → "Static Site"
   - Conecta el mismo repositorio
   
   **Configuración:**
   ```
   Name: metal-veneta-dashboard
   Build Command: (dejar vacío o npm install si usas npm)
   Publish Directory: frontend
   ```

2. **Actualizar JavaScript para usar la URL del backend**
   - En `frontend/assets/js/api.js`, cambiar:
   ```javascript
   const API_URL = 'https://metal-veneta-api.onrender.com';
   ```

3. **¡Deploy!** Tendrás una URL como:
   ```
   https://metal-veneta-dashboard.onrender.com
   ```

---

### Opción 2: Railway (Alternativa Moderna)

#### Backend

1. **Crear cuenta en Railway**
   - https://railway.app
   - Login con GitHub

2. **Nuevo Proyecto**
   - "New Project" → "Deploy from GitHub"
   - Selecciona tu repo

3. **Configurar**
   - Railway detectará automáticamente Python
   - Asegúrate de que el comando sea:
     ```
     Start Command: cd backend && python api/main.py
     ```

4. **Variables**
   - Railway inyecta PORT automáticamente
   - Agregar al main.py:
     ```python
     port = int(os.environ.get("PORT", 8000))
     uvicorn.run(app, host="0.0.0.0", port=port)
     ```

5. **URL del backend**
   ```
   https://metal-veneta-api.railway.app
   ```

#### Frontend

1. **Nuevo Static Site**
   - "New" → "Empty Project" → "Generate Domain"
   - Agregar archivos del frontend

2. **URL del frontend**
   ```
   https://metal-veneta-dashboard.railway.app
   ```

---

### Opción 3: Vercel (Para Frontend) + Render (Para Backend)

**Mejor combinación:**
- **Backend**: Render (gratis y confiable)
- **Frontend**: Vercel (gratis y rápido)

#### Vercel para Frontend

1. **Crear cuenta**
   - https://vercel.com
   - Login con GitHub

2. **Import Project**
   - Selecciona tu repositorio
   - Framework Preset: Other
   - Root Directory: `frontend`

3. **Deploy!**
   - URL: `https://metal-veneta-dashboard.vercel.app`

---

## 📝 Checklist Pre-Deploy

### Backend

- [x] Instalar dependencias en `requirements-api.txt`
- [x] Probar API localmente (`python backend/api/main.py`)
- [x] Verificar que `/api/rendimientos` funciona
- [ ] Subir código a GitHub
- [ ] Crear servicio en Render/Railway
- [ ] Copiar URL del backend

### Frontend

- [ ] Crear HTML base (`frontend/index.html`)
- [ ] Agregar JavaScript para consumir API
- [ ] Actualizar URL del backend en código JS
- [ ] Agregar estilos CSS
- [ ] Probar localmente
- [ ] Subir a Vercel/Render

### QR Code

1. **Una vez deployado, generar QR**
   - Ir a https://www.qr-code-generator.com
   - Pegar URL del frontend deployado
   - Descargar imagen QR
   - Incluir en presentación

---

## 🔧 Troubleshooting

### Error: CORS
**Solución**: Ya está configurado en `main.py` con CORSMiddleware

### Error: No se encuentra el archivo Excel
**Solución**: Asegúrate de que el Excel esté en el repositorio o en el despliegue

### Error: Puerto ya en uso
**Solución**: Render/Railway asigna puerto automáticamente

### API lenta
**Solución**: Render en plan free puede "dormirse" después de 15 min sin uso. Primera request toma más tiempo.

---

## 🎯 URL Final

Una vez deployado:

**Backend API**: `https://metal-veneta-api.onrender.com`  
**Frontend Dashboard**: `https://metal-veneta-dashboard.vercel.app`  
**QR Code**: Apunta al frontend

---

## 📸 Preparar para Presentación

1. **Probar en móvil**
   - Abrir URL en teléfono
   - Verificar que todo funcione

2. **Plan B**
   - Tener capturas de pantalla
   - Video de demostración
   - Backup local del proyecto

3. **Prueba de conectividad**
   - WiFi del lugar de presentación
   - Datos móviles como backup

---

**¿Listo para deployar?** 🔥
