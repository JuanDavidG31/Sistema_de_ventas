# Sistema Web de Ventas para una Distribuidora de Juguetes

---

##  Descripción General
Desarrollo de un **sistema web de ventas** para una **distribuidora de juguetes con cobertura nacional**.  
El sistema permitirá gestionar **ventas, inventario, clientes y productos**, con un enfoque en la eficiencia del manejo de datos.  
La solución utiliza **Django (Python)** para el backend y **Angular** para el frontend, integrando bases de datos **relacional (MySQL/MariaDB)** y **NoSQL** para el manejo de imágenes.

---

##  Objetivos Específicos
- Diseñar e implementar una **base de datos relacional optimizada**.  
- Diseñar una **base de datos NoSQL** para el almacenamiento de imágenes de productos.  
- Desarrollar el **backend con Django (Python)**.  
- Construir un **frontend responsivo en Angular**.  
- Implementar los **procedimientos y scripts** necesarios para poblar la base de datos.  
- Gestionar el **seguimiento del proyecto por sesiones planificadas**.

---

##  Arquitectura Tecnológica

###  Backend
- **Lenguaje:** Python 3.8+  
- **Framework:** Django  
- **ORM:** SQLAlchemy  
- **Base de datos:** MySQL / MariaDB  
- **API:** Django REST Framework  

###  Frontend
- **Framework:** Angular  
- **Lenguajes:** HTML5, CSS3, TypeScript  
- **Diseño:** Bootstrap 5  
- **Gráficos:** Chart.js  

###  Herramientas de Desarrollo
- Git (Control de versiones)  
- Virtualenv (Entornos virtuales)  
- SQLAlchemy Migrate (Migraciones de base de datos)

---

##  Módulos Principales

###  Módulo de Ventas
Pantalla de venta dividida en tres secciones:

**Encabezado**
- Fecha y hora automática  
- Selección de cliente con búsqueda  
- Número de factura automático  
- Forma de pago (contado / crédito)

**Detalle**
- Búsqueda de productos por código o nombre  
- Campos: código, cantidad, valor unitario, IVA, total  
- Cálculos automáticos de subtotales e impuestos  

**Pie de Página**
- Totales de productos, IVA y general  

---

###  Mantenimiento de Tablas Maestras
CRUD completo para:
- **Clientes:** clasificados por ubicación (municipio y departamento) y tipo de pago (crédito, contado o mixto).  
- **Productos:** agrupados por líneas de producto.  
- **Líneas de producto:** con gestión completa desde la interfaz.

---

###  Módulo de Reportes
Generación de al menos **5 reportes estadísticos o de resumen** que reflejen el estado del sistema (no reportes de detalle).  
Ejemplos:
- Ventas por departamento o línea de producto  
- Productos más vendidos  
- Clientes activos  
- Comparativos mensuales  
- Estadísticas de inventario

---

##  Diseño de Base de Datos

###  Modelo Entidad–Relación
Entidades principales:
- Departamentos  
- Municipios  
- Clientes  
- Líneas de producto  
- Productos  
- Ventas  

###  Modelo Relacional
- Conversión del modelo E–R con normalización  
- Creación de índices e integridad referencial  
- Definición de claves primarias y foráneas  

###  Base de Datos NoSQL
- Utilizada para almacenar **imágenes de productos**  
- Justificación: mejora el rendimiento, la escalabilidad y reduce la carga de la base relacional.

---

##  Procedimientos y Scripts
- Creación de un **script en Python** para poblar las bases de datos (relacional y NoSQL).  
- Automatización de inserción y validación de datos.  
- Procedimientos de carga inicial para pruebas funcionales.

---

## Criterios de Aceptación

### 🔹 Backend
- API REST funcional  
- Validación de datos  
- Manejo de errores  
- Transacciones seguras  
- Scripts de población funcionando correctamente

### 🔹 Frontend
- Interfaz **responsiva y amigable**  
- Pantalla de ventas funcional con cálculos automáticos  
- CRUDs administrativos completos  
- Módulo de reportes activo e integrado  

### 🔹 Base de Datos
- Modelo relacional implementado  
- Integridad referencial garantizada  
- Índices optimizados  
- Datos de prueba cargados  
- Integración NoSQL funcional  

---

##  Plan de Sesiones

| Sesión | Tema | Fecha |
|:-------|:------|:-------|
| 1 | Diseño Conceptual (modelo E–R, requisitos, NoSQL) | **Nov. 6** |
| 2 | Implementación BD + Backend base | **Nov. 7** |
| 3 | Módulo de Ventas | **Nov. 11** |
| 4 | Módulos Administrativos | **Nov. 13** |
| 5 | Reportes y Pulimiento | **Nov. 14** |
| 6 | Sustentación | **Nov. 18** |

---

