# 🚀 Odoo Power BI API Connector (FastAPI + Nginx + Redis)

Este proyecto expone una API REST usando **FastAPI**, con **Nginx como proxy reverso** y **Redis como sistema de cache**, diseñada para consumir datos de un servidor remoto de **Odoo** y permitir su conexión desde herramientas como **Power BI**.

---

## 🧱 Estructura del Proyecto

```
odoo-powerbi-api/
├── docker-compose.yml
├── nginx/
│   └── default.conf
├── fastapi_app/
│   ├── Dockerfile
│   ├── main.py
│   ├── odoo_rpc.py
│   └── redis_cache.py
└── requirements.txt
```

---

## 🐳 Docker Compose

### Servicios

- **fastapi**: API REST que se conecta a Odoo vía XML-RPC.
- **nginx**: Proxy reverso para exponer FastAPI en el puerto 80.
- **redis**: Sistema de almacenamiento en caché.

---

## ⚙️ Variables de Entorno

Define en `docker-compose.yml` las siguientes variables para conectar al Odoo remoto:

```yaml
ODOO_URL=http://<host-odoo>:8069
ODOO_DB=nombre_base_datos
ODOO_USER=usuario_odoo
ODOO_PASSWORD=clave_odoo
REDIS_HOST=redis
```

---

## 🚀 Levantar el Proyecto

```bash
docker-compose up --build
```

Accede a la API en:

- 🌐 http://localhost/

---

## 🧠 Endpoints disponibles

| Método | Endpoint         | Descripción                             |
|--------|------------------|-----------------------------------------|
| GET    | `/`              | Mensaje de bienvenida                   |
| GET    | `/partners?limit=10` | Lista de partners (empresas) desde Odoo |

---

## 📊 Conexión con Power BI

1. Abre Power BI Desktop.
2. Ir a **Inicio → Obtener datos → Web**.
3. Ingresa la URL: `http://localhost/partners`
4. Carga los datos como tabla JSON.

---

## 🧩 Extensiones posibles

- 🔐 Autenticación por token (JWT)
- 📄 Más endpoints: ventas, facturas, productos, etc.
- 🔒 HTTPS con Let's Encrypt
- 🧠 Cache selectiva con expiración por modelo

---

## 📜 Licencia

MIT © TuNombre
