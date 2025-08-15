# ==========================================
# SETUP PYTHON + FASTAPI PARA RAILWAY
# ==========================================

# PASO 1: Crear estructura del proyecto
mkdir pizzeria-dashboard-python
cd pizzeria-dashboard-python

# PASO 2: Crear archivos principales
touch main.py
touch requirements.txt
touch .gitignore
mkdir static
touch static/index.html
mkdir templates

# PASO 3: Crear requirements.txt
cat > requirements.txt << 'EOF'
fastapi==0.104.1
uvicorn[standard]==0.24.0
psycopg2-binary==2.9.9
python-multipart==0.0.6
jinja2==3.1.2
python-dotenv==1.0.0
pydantic==2.5.0
httpx==0.25.2
EOF

# PASO 4: Crear .gitignore
cat > .gitignore << 'EOF'
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST
.env
.env.local
.venv
env/
venv/
ENV/
env.bak/
venv.bak/
.DS_Store
*.log
EOF

# PASO 5: Crear entorno virtual (opcional para desarrollo local)
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt

echo "✅ Estructura Python creada"
echo "🐍 FastAPI listo para Railway"
echo "🚀 Siguiente paso: Configurar main.py"