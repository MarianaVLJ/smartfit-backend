
# SmartFit Backend API - Clean Architecture & DDD

Backend desarrollado en Python utilizando **Flask** y **SQLAlchemy**, diseñado bajo los principios de **Clean Architecture** y **Domain-Driven Design (DDD)**. Este sistema gestiona el núcleo operativo para una cadena de gimnasios, abarcando desde el control perimetral y registro de socios hasta la adquisición de membresías y la gestión de accesos contingenciales por fallos biométricos.



## Enfoque Arquitectónico (DDD & Clean Architecture)

El proyecto implementa una separación estricta de responsabilidades en capas concéntricas, asegurando que el **Dominio** (las reglas de negocio puras) sea completamente independiente de los frameworks, la base de datos o la interfaz de usuario:

1. **Capa de Dominio (`domain/`):** Contiene las entidades y las reglas de negocio fundamentales del sistema de gimnasio.
2. **Capa de Aplicación (`application/`):** Orquesta los casos de uso y los servicios que resuelven los requerimientos funcionales.
3. **Capa de Infraestructura (`infrastructure/`):** Gestiona los detalles técnicos externos, incluyendo los modelos ORM de **SQLAlchemy**, la conexión a **SQLite** y la implementación de los repositorios de datos.
4. **Capa de Presentación (`presentation/`):** Expone la interfaz de comunicación mediante controladores REST estructurados como **Blueprints de Flask**.



## Estructura del Repositorio

```text
smartfit-backend/
│
├── src/
│   ├── domain/               # Entidades y reglas de negocio puras
│   │
│   ├── application/          # Servicios de aplicación y lógica de casos de uso
│   │   └── services/
│   │       ├── cliente_service.py
│   │       └── suscripcion_service.py
│   │
│   ├── infrastructure/       # Capa de datos y persistencia (ORM & Repositorios)
│   │   ├── database.py       # Instancia centralizada de SQLAlchemy
│   │   ├── models/
│   │   │   ├── socio_model.py
│   │   │   └── suscripcion_model.py
│   │   └── repositories/
│   │       ├── cliente_repository.py
│   │       └── suscripcion_repository.py
│   │
│   └── presentation/         # Controladores y puntos de entrada HTTP (API REST)
│       └── controllers/
│           ├── cliente_controller.py
│           └── suscripcion_controller.py
│
├── Pruebas de API/           # Colecciones BDD exportadas en formato JSON (Postman)
├── app.py                    # Punto de entrada principal y registro central de Blueprints
├── requirements.txt          # Dependencias y librerías del proyecto
└── smartfit.db               # Base de datos relacional SQLite (Generada automáticamente)

```

---

## Tecnologías y Herramientas Utilizadas

* **Python** (Lenguaje de programación principal)
* **Flask** (Microframework web orientado a servicios REST)
* **Flask-SQLAlchemy** (ORM para el mapeo objeto-relacional y persistencia)
* **SQLite** (Base de datos relacional ligera para desarrollo y pruebas)
* **Postman** (Herramienta para pruebas funcionales y de aceptación bajo enfoque BDD)

---

## Diagrama de Flujo del Sistema

```text
+-----------------------------------------------------------------------+
|                          PRESENTATION LAYER                           |
|       (cliente_controller.py / suscripcion_controller.py [Blueprints])|
+-----------------------------------------------------------------------+
                                   │
                                   ▼
+-----------------------------------------------------------------------+
|                          APPLICATION LAYER                            |
|             (cliente_service.py / suscripcion_service.py)             |
+-----------------------------------------------------------------------+
                                   │
                                   ▼
+-----------------------------------------------------------------------+
|                         INFRASTRUCTURE LAYER                          |
|         (Repositorios + Modelos ORM: SocioModel, Suscripcion, etc.)   |
+-----------------------------------------------------------------------+
                                   │
                                   ▼
+-----------------------------------------------------------------------+
|                          DATABASE PERSISTENCE                         |
|                     (SQLite Engine -> smartfit.db)                    |
+-----------------------------------------------------------------------+

```

---

## Instrucciones de Instalación y Ejecución

1. **Clonar el repositorio:**
```bash
git clone <URL_DEL_REPOSITORIO>
cd smartfit-backend

```


2. **Crear y activar el entorno virtual:**
```bash
python -m venv venv
# En Windows (PowerShell):
.\venv\Scripts\Activate

```


3. **Instalar las dependencias:**
```bash
pip install -r requirements.txt

```


4. **Ejecutar la aplicación:**
```bash
python app.py

```


*El servidor local se iniciará en `http://127.0.0.1:5000` y creará de forma automatizada el archivo `smartfit.db` con todas las tablas requeridas por los modelos ORM.*

---

##  Documentación de Endpoints del API REST

### 1. Módulo de Socios / Clientes

* **`POST /socios`**
* *Descripción:* Registra un nuevo socio en el sistema con su DNI, datos personales y estado.


* **`GET /socios/<dni>`**
* *Descripción:* Consulta la información detallada de un socio específico utilizando su DNI.


* **`PUT /socios/<dni>`**
* *Descripción:* Actualiza los datos o el estado de membresía de un socio existente.


* **`DELETE /socios/<dni>`**
* *Descripción:* Da de baja o elimina lógicamente a un socio del sistema.



### 2. Módulo de Suscripciones y Acceso Contingencial

* **`POST /suscripciones`**
* *Descripción:* Asigna y registra una membresía (ej. Plan Black) a un socio activo.
* *Ejemplo de Body (JSON):*
```json
{
    "dni": "71234567",
    "plan": "Black",
    "fecha_inicio": "2026-07-21"
}

```




* **`GET /suscripciones`**
* *Descripción:* Retorna el listado completo de todas las suscripciones registradas en la base de datos.


* **`POST /contingencia`**
* *Descripción:* Registra un acceso excepcional de emergencia cuando falla la validación biométrica del socio en puerta.
* *Ejemplo de Body (JSON):*
```json
{
    "dni": "71234567",
    "motivo": "Falla biométrica"
}

```




* **`GET /contingencia`**
* *Descripción:* Consulta el historial completo de accesos contingenciales registrados.



---

##  Pruebas de Aceptación (BDD)

Las colecciones de pruebas funcionales diseñadas bajo criterios de aceptación orientados al comportamiento (**Given-When-Then**) se encuentran exportadas en formato JSON y almacenadas dentro de la carpeta **`Pruebas de API/`** en la raíz de este repositorio, listas para su importación en Postman o ejecución mediante herramientas automatizadas.

---

## Equipo de Desarrollo

* **Mariana Luis** - Arquitectura base, Módulo de Socios y Control de Acceso Perimetral.
* **Claudia Agostinelli** - Módulo de Adquisición de Suscripciones y Gestión de Acceso Contingencial.

```

```
