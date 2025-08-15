# ==========================================
# BACKEND PYTHON FASTAPI PARA RAILWAY
# Archivo: main.py
# ==========================================

import os
import json
from datetime import datetime, date
from typing import List, Optional
import psycopg2
from psycopg2.extras import RealDictCursor
from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn
from dotenv import load_dotenv

load_dotenv()

# ==========================================
# MODELOS PYDANTIC
# ==========================================

class ProductoBase(BaseModel):
    nombre: str
    cantidad: int
    precio_unitario: float
    modificaciones: Optional[str] = ""
    subtotal: float

class PedidoNuevo(BaseModel):
    telefono_cliente: str
    nombre_cliente: str
    productos: List[ProductoBase]
    subtotal: float
    costo_envio: float = 30.0
    total: float
    direccion_entrega: str
    notas_cliente: Optional[str] = ""

class ActualizarEstado(BaseModel):
    estado: str
    notas: Optional[str] = ""

# ==========================================
# CONFIGURACIÓN BASE DE DATOS
# ==========================================

def get_db_connection():
    """Obtener conexión a PostgreSQL"""
    try:
        connection = psycopg2.connect(
            os.getenv("DATABASE_URL"),
            cursor_factory=RealDictCursor
        )
        return connection
    except Exception as e:
        print(f"❌ Error conectando a la base de datos: {e}")
        raise e
def get_db_schema():
    """Obtener el esquema de la base de datos (por defecto 'public')"""
    return os.getenv("DB_SCHEMA", "public")

async def initialize_database():
    """Inicializar tablas y datos de ejemplo"""
    try:
        print("🔄 Inicializando base de datos...")
        
        conn = get_db_connection()
        cursor = conn.cursor()
        
        schema = get_db_schema()
        cursor.execute(f"CREATE SCHEMA IF NOT EXISTS {schema};")
        
        # Crear tablas en el esquema elegido
        cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {schema}.productos (
                id SERIAL PRIMARY KEY,
                nombre VARCHAR(255) NOT NULL,
                descripcion TEXT,
                precio DECIMAL(10,2) NOT NULL,
                categoria VARCHAR(100),
                disponible BOOLEAN DEFAULT true,
                imagen_url TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)
        
        cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {schema}.clientes (
                id SERIAL PRIMARY KEY,
                telefono VARCHAR(20) UNIQUE NOT NULL,
                nombre VARCHAR(255),
                direccion_default TEXT,
                total_pedidos INTEGER DEFAULT 0,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)
        
        cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {schema}.pedidos (
                id SERIAL PRIMARY KEY,
                numero_pedido VARCHAR(20) UNIQUE NOT NULL,
                cliente_id INTEGER REFERENCES {schema}.clientes(id),
                telefono_cliente VARCHAR(20) NOT NULL,
                nombre_cliente VARCHAR(255),
                productos_json JSONB NOT NULL,
                subtotal DECIMAL(10,2) NOT NULL,
                costo_envio DECIMAL(10,2) DEFAULT 30.00,
                total DECIMAL(10,2) NOT NULL,
                direccion_entrega TEXT NOT NULL,
                estado VARCHAR(50) DEFAULT 'pendiente',
                notas_cliente TEXT,
                notas_internas TEXT,
                tiempo_estimado INTEGER DEFAULT 45,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)
        
        cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {schema}.historial_pedidos (
                id SERIAL PRIMARY KEY,
                pedido_id INTEGER REFERENCES {schema}.pedidos(id) ON DELETE CASCADE,
                estado_anterior VARCHAR(50),
                estado_nuevo VARCHAR(50) NOT NULL,
                usuario VARCHAR(100) DEFAULT 'Sistema',
                notas TEXT,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)
        
        # Verificar si hay productos
        cursor.execute(f"SELECT COUNT(*) FROM {schema}.productos")
        productos_count = cursor.fetchone()['count']
        
        if productos_count == 0:
            print("📦 Insertando productos de ejemplo...")
            await insert_sample_data(cursor, schema)
        
        conn.commit()
        cursor.close()
        conn.close()
        
        print("✅ Base de datos inicializada correctamente")
        
    except Exception as e:
        print(f"❌ Error inicializando base de datos: {e}")
        raise e

async def insert_sample_data(cursor, schema):
    """Insertar datos de ejemplo"""
    productos = [
        ('Pizza Margarita Chica', 'Salsa de tomate, mozzarella, albahaca fresca', 180.00, 'Pizzas'),
        ('Pizza Margarita Grande', 'Salsa de tomate, mozzarella, albahaca fresca', 280.00, 'Pizzas'),
        ('Pizza Pepperoni Chica', 'Salsa de tomate, mozzarella, pepperoni', 220.00, 'Pizzas'),
        ('Pizza Pepperoni Grande', 'Salsa de tomate, mozzarella, pepperoni', 320.00, 'Pizzas'),
        ('Pizza Hawaiana Chica', 'Salsa de tomate, mozzarella, jamón, piña', 240.00, 'Pizzas'),
        ('Pizza Hawaiana Grande', 'Salsa de tomate, mozzarella, jamón, piña', 340.00, 'Pizzas'),
        ('Coca Cola 600ml', 'Refresco de cola', 35.00, 'Bebidas'),
        ('Agua Natural 500ml', 'Agua purificada', 20.00, 'Bebidas'),
        ('Papas Fritas', 'Papas fritas crujientes', 60.00, 'Complementos'),
        ('Pan de Ajo', 'Pan tostado con ajo y mantequilla', 50.00, 'Complementos')
    ]
    
    for producto in productos:
        cursor.execute(
            f"INSERT INTO {schema}.productos (nombre, descripcion, precio, categoria) VALUES (%s, %s, %s, %s)",
            producto
        )
    
    # Pedidos de ejemplo
    pedidos_ejemplo = [
        {
            'numero_pedido': 'ORD-001',
            'telefono_cliente': '+5215512345678',
            'nombre_cliente': 'María García',
            'productos_json': json.dumps([
                {'nombre': 'Pizza Pepperoni Grande', 'cantidad': 1, 'precio_unitario': 320, 'subtotal': 320},
                {'nombre': 'Coca Cola 600ml', 'cantidad': 2, 'precio_unitario': 35, 'subtotal': 70}
            ]),
            'subtotal': 390,
            'total': 420,
            'direccion_entrega': 'Av. Reforma 123, Col. Centro, CDMX',
            'estado': 'pendiente'
        },
        {
            'numero_pedido': 'ORD-002',
            'telefono_cliente': '+5215587654321',
            'nombre_cliente': 'Carlos López',
            'productos_json': json.dumps([
                {'nombre': 'Pizza Margarita Grande', 'cantidad': 1, 'precio_unitario': 280, 'subtotal': 280}
            ]),
            'subtotal': 280,
            'total': 310,
            'direccion_entrega': 'Calle Insurgentes 456, Col. Roma Norte, CDMX',
            'estado': 'preparando'
        }
    ]
    
    for pedido in pedidos_ejemplo:
        cursor.execute(f"""
            INSERT INTO {schema}.pedidos (
                numero_pedido, telefono_cliente, nombre_cliente, productos_json,
                subtotal, total, direccion_entrega, estado
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            pedido['numero_pedido'], pedido['telefono_cliente'], pedido['nombre_cliente'],
            pedido['productos_json'], pedido['subtotal'], pedido['total'],
            pedido['direccion_entrega'], pedido['estado']
        ))

# ==========================================
# CONFIGURACIÓN FASTAPI
# ==========================================

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    await initialize_database()
    yield
    # Shutdown

app = FastAPI(
    title="Pizzería Dashboard API",
    description="API para gestión de pedidos de pizzería",
    version="1.0.0",
    lifespan=lifespan
)

# Servir archivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")

# Modificar o agregar la ruta principal:
@app.get("/", response_class=HTMLResponse)
async def dashboard():
    """Servir el dashboard principal"""
    try:
        return FileResponse("static/index.html")
    except FileNotFoundError:
        return HTMLResponse("""
        <h1>🍕 Pizzería Dashboard</h1>
        <p><strong>Error:</strong> No se encontró el archivo static/index.html</p>
        <p>Asegúrate de crear la carpeta 'static' y el archivo 'index.html' dentro.</p>
        <div style="margin: 20px 0; padding: 15px; background: #f0f0f0; border-radius: 8px;">
            <h3>📁 Estructura necesaria:</h3>
            <pre>
pizzeria-dashboard-python/
├── main.py
├── requirements.txt
└── static/
    └── index.html  ← CREAR ESTE ARCHIVO
            </pre>
        </div>
        <p><a href="/api/health">🔍 Ver API Health Check</a></p>
        <p><a href="/api/pedidos">📋 Ver Pedidos API</a></p>
        """)


# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Servir archivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")

# ==========================================
# RUTAS API
# ==========================================

@app.get("/api/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "OK",
        "timestamp": datetime.now().isoformat(),
        "environment": os.getenv("ENVIRONMENT", "development")
    }

@app.get("/api/pedidos")
async def obtener_pedidos():
    """Obtener todos los pedidos activos"""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT 
                p.id,
                p.numero_pedido,
                p.nombre_cliente,
                p.telefono_cliente,
                p.productos_json,
                p.subtotal,
                p.costo_envio,
                p.total,
                p.estado,
                p.direccion_entrega,
                p.notas_cliente,
                p.notas_internas,
                p.created_at,
                EXTRACT(EPOCH FROM (NOW() - p.created_at))/60 as minutos_transcurridos
            FROM pedidos p 
            WHERE p.estado IN ('pendiente', 'preparando', 'listo')
            ORDER BY p.created_at DESC
        """)
        
        pedidos = cursor.fetchall()
        cursor.close()
        conn.close()
        
        return {
            "success": True,
            "pedidos": [dict(pedido) for pedido in pedidos],
            "total": len(pedidos)
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error obteniendo pedidos: {str(e)}")

@app.put("/api/pedidos/{numero}/estado")
async def actualizar_estado_pedido(numero: str, estado_data: ActualizarEstado):
    """Actualizar estado de un pedido"""
    try:
        conn = get_db_connection()
        schema = get_db_schema()
        cursor = conn.cursor()
        
        # Obtener estado anterior
        cursor.execute(f"SELECT estado FROM {schema}.pedidos WHERE numero_pedido = %s", (numero,))
        resultado = cursor.fetchone()
        
        if not resultado:
            raise HTTPException(status_code=404, detail="Pedido no encontrado")
        
        estado_anterior = resultado['estado']
        
        # Actualizar pedido
        cursor.execute(
            f"UPDATE {schema}.pedidos SET estado = %s, updated_at = NOW() WHERE numero_pedido = %s",
            (estado_data.estado, numero)
        )
        
        # Registrar en historial
        cursor.execute(f"""
            INSERT INTO {schema}.historial_pedidos (
                pedido_id, estado_anterior, estado_nuevo, notas, usuario
            ) 
            SELECT id, %s, %s, %s, %s 
            FROM pedidos 
            WHERE numero_pedido = %s
        """, (estado_anterior, estado_data.estado, estado_data.notas or "", "Dashboard", numero))
        
        conn.commit()
        cursor.close()
        conn.close()
        
        return {
            "success": True,
            "message": f"Pedido {numero} actualizado de '{estado_anterior}' a '{estado_data.estado}'"
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error actualizando estado: {str(e)}")

@app.get("/api/estadisticas")
async def obtener_estadisticas():
    """Obtener estadísticas del día"""
    try:
        conn = get_db_connection()
        schema = get_db_schema()
        cursor = conn.cursor()
        
        cursor.execute(f"""
            SELECT 
                COUNT(*) as total_pedidos,
                COALESCE(SUM(total), 0) as ingresos_dia,
                COALESCE(AVG(total), 0) as ticket_promedio,
                COUNT(*) FILTER (WHERE estado = 'pendiente') as pendientes,
                COUNT(*) FILTER (WHERE estado = 'preparando') as preparando,
                COUNT(*) FILTER (WHERE estado = 'listo') as listos,
                COUNT(*) FILTER (WHERE estado = 'entregado') as entregados
            FROM {schema}.pedidos 
            WHERE DATE(created_at) = CURRENT_DATE
        """)
        
        estadisticas = cursor.fetchone()
        cursor.close()
        conn.close()
        
        return {
            "success": True,
            "estadisticas": dict(estadisticas)
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error obteniendo estadísticas: {str(e)}")

@app.post("/api/pedido-nuevo")
async def crear_pedido_nuevo(pedido: PedidoNuevo):
    """Crear nuevo pedido (webhook desde n8n)"""
    try:
        conn = get_db_connection()
        schema = get_db_schema()
        cursor = conn.cursor()
        
        # Generar número de pedido
        cursor.execute(f"""
            SELECT 'ORD-' || LPAD(
                (COALESCE(MAX(CAST(SUBSTRING(numero_pedido FROM 5) AS INTEGER)), 0) + 1)::TEXT, 
                3, '0'
            ) as nuevo_numero
            FROM {schema}.pedidos 
            WHERE DATE(created_at) = CURRENT_DATE
        """)
        numero_pedido = cursor.fetchone()['nuevo_numero']
        
        # Convertir productos a JSON
        productos_json = json.dumps([producto.dict() for producto in pedido.productos])
        
        # Insertar pedido
        cursor.execute(f"""
            INSERT INTO {schema}.pedidos (
                numero_pedido, telefono_cliente, nombre_cliente, productos_json,
                subtotal, costo_envio, total, direccion_entrega, notas_cliente, estado
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, 'pendiente')
            RETURNING id, numero_pedido
        """, (
            numero_pedido, pedido.telefono_cliente, pedido.nombre_cliente, productos_json,
            pedido.subtotal, pedido.costo_envio, pedido.total, 
            pedido.direccion_entrega, pedido.notas_cliente
        ))
        
        resultado = cursor.fetchone()
        conn.commit()
        cursor.close()
        conn.close()
        
        return {
            "success": True,
            "pedido": dict(resultado),
            "message": f"Pedido {numero_pedido} creado exitosamente"
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creando pedido: {str(e)}")

# ==========================================
# RUTA PRINCIPAL (DASHBOARD)
# ==========================================

@app.get("/", response_class=HTMLResponse)
async def dashboard():
    """Servir el dashboard principal"""
    try:
        return FileResponse("static/index.html")
    except FileNotFoundError:
        return HTMLResponse("""
        <h1>🍕 Pizzería Dashboard</h1>
        <p>Dashboard no encontrado. Asegúrate de tener el archivo static/index.html</p>
        <p><a href="/api/health">Ver API Health Check</a></p>
        <p><a href="/api/pedidos">Ver Pedidos API</a></p>
        """)

# ==========================================
# INICIALIZACIÓN
# ==========================================

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(
        "main:app", 
        host="0.0.0.0", 
        port=port, 
        reload=False
    )