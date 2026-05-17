# Documentación Proyecto Final DevOps

# 1. Pipeline CI/CD

## Objetivo
El objetivo del pipeline CI/CD es automatizar procesos de integración continua para validar el funcionamiento del proyecto cada vez que se realizan cambios en el repositorio.

## Herramientas utilizadas
- GitHub Actions
- Docker
- Pytest
- Python 3.11

## Funcionamiento del pipeline
El pipeline fue implementado utilizando GitHub Actions mediante el archivo:

```text
.github/workflows/ci-cd.yml
```

Cada vez que se realiza un push o pull request hacia la rama principal (`main`), GitHub ejecuta automáticamente el flujo de integración continua.

## Etapas del pipeline

### 1. Clonado del repositorio
GitHub Actions descarga automáticamente el código fuente del proyecto.

### 2. Configuración de Python
Se instala Python 3.11 en el entorno temporal de ejecución.

### 3. Instalación de dependencias
El pipeline instala todas las librerías necesarias utilizando:

```bash
pip install -r requirements.txt
```

### 4. Ejecución de pruebas unitarias
Se ejecutan las pruebas automatizadas con pytest:

```bash
pytest -v
```

Esto permite validar el correcto funcionamiento de los endpoints de la API.

### 5. Construcción de imagen Docker
El pipeline construye automáticamente la imagen Docker utilizando:

```bash
docker build -t todo-api .
```

Esto garantiza que la aplicación pueda contenerizarse correctamente.

## Beneficios del CI/CD
- Automatización de validaciones
- Detección temprana de errores
- Integración continua
- Mayor calidad del software
- Reducción de errores manuales

---

# 2. Observabilidad

## Objetivo
Implementar mecanismos de monitoreo y observabilidad para conocer el estado y comportamiento de la API.

## Health Check
Se implementó un endpoint `/health` que permite verificar rápidamente si la aplicación se encuentra funcionando correctamente.

### Endpoint

```text
/health
```

### Respuesta esperada

```json
{
  "status": "healthy"
}
```

## Logs estructurados
Se configuró logging en Flask utilizando la librería estándar de Python.

### Configuración utilizada

```python
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s'
)
```

## Función de los logs
Los logs permiten:
- Monitorear solicitudes HTTP
- Registrar eventos importantes
- Facilitar diagnóstico de errores
- Realizar trazabilidad del sistema

## Métricas con Prometheus
Se integró `prometheus-flask-exporter` para generar métricas automáticas.

### Endpoint

```text
/metrics
```

## Métricas generadas
Algunas métricas disponibles son:
- Cantidad de solicitudes HTTP
- Tiempo de respuesta
- Uso de CPU
- Uso de memoria
- Excepciones HTTP

## Beneficios de observabilidad
- Monitoreo en tiempo real
- Detección temprana de fallos
- Análisis de rendimiento
- Soporte para herramientas como Prometheus y Grafana

---

# 3. Seguridad

## Objetivo
Implementar herramientas básicas de análisis de seguridad y calidad del código.

## Auditoría de dependencias
Se utilizó la herramienta `pip-audit` para identificar vulnerabilidades conocidas en las dependencias Python.

### Comando utilizado

```bash
pip-audit
```

## Resultado
La herramienta permitió detectar CVEs asociados a algunas versiones de dependencias instaladas.

## Importancia
La auditoría de dependencias ayuda a:
- Detectar vulnerabilidades conocidas
- Reducir riesgos de seguridad
- Mantener librerías actualizadas
- Mejorar la seguridad del proyecto

## Linting con flake8
Se implementó análisis estático del código utilizando flake8.

### Comando utilizado

```bash
flake8 src
```

## Función del linting
El linting permite:
- Detectar malas prácticas
- Validar estándares de estilo
- Mejorar legibilidad del código
- Identificar errores potenciales

## Resultado obtenido
Se encontraron advertencias relacionadas principalmente con longitud de líneas (`E501 line too long`).

---

# 4. Docker y Contenerización

## Objetivo
Contenerizar la aplicación para garantizar portabilidad y reproducibilidad.

## Dockerfile
Se creó un Dockerfile para construir una imagen de la aplicación Flask.

## Imagen base utilizada

```dockerfile
FROM python:3.11-slim
```

## Funciones principales del Dockerfile
- Instalar dependencias
- Copiar archivos del proyecto
- Configurar el entorno de ejecución
- Ejecutar la API Flask

## Docker Compose
Se utilizó Docker Compose para automatizar el despliegue del contenedor.

### Archivo utilizado

```text
docker-compose.yml
```

## Funcionalidades implementadas
- Construcción automática de imagen
- Configuración de variables de entorno
- Exposición de puertos
- Reinicio automático del contenedor

## Beneficios de Docker
- Portabilidad
- Consistencia entre entornos
- Facilidad de despliegue
- Aislamiento de dependencias

---

# 5. Tests Unitarios

## Objetivo
Validar automáticamente el comportamiento de la API.

## Herramienta utilizada
- Pytest

## Cantidad de pruebas implementadas
Se implementaron 5 pruebas unitarias.

## Pruebas realizadas

### 1. test_home
Valida que el endpoint principal responda correctamente.

### 2. test_get_tasks
Verifica el listado de tareas.

### 3. test_create_task
Comprueba la creación exitosa de una tarea.

### 4. test_create_task_without_title
Valida manejo de errores cuando falta el campo obligatorio `title`.

### 5. test_task_not_found
Verifica la respuesta ante consultas de tareas inexistentes.

## Resultado
Todas las pruebas fueron exitosas:

```text
5 passed
```

## Beneficios de pruebas unitarias
- Validación automática
- Detección temprana de errores
- Mayor confiabilidad
- Facilita integración continua

---

# 6. CALMS en DevOps

## ¿Qué es CALMS?
CALMS es un modelo utilizado en DevOps para evaluar buenas prácticas en cinco áreas fundamentales:

- Culture
- Automation
- Lean
- Measurement
- Sharing

## Culture
Se promovió trabajo colaborativo mediante GitHub y control de versiones.

## Automation
Se automatizaron:
- pruebas unitarias
- construcción Docker
- ejecución del pipeline CI/CD

## Lean
Se utilizaron contenedores ligeros (`python:3.11-slim`) para optimizar recursos.

## Measurement
Se implementaron métricas y monitoreo mediante Prometheus y logging.

## Sharing
Toda la documentación y el código fueron compartidos mediante GitHub.

---

# 7. Estrategia de Branching

## Objetivo
Mantener control de versiones y organización del desarrollo.

## Rama principal
Se utilizó la rama `main` como rama principal del proyecto.

## Flujo de trabajo
Los cambios fueron:
1. desarrollados localmente,
2. versionados con Git,
3. confirmados mediante commits,
4. enviados al repositorio remoto con push.

## Comandos utilizados

### Agregar cambios

```bash
git add .
```

### Crear commit

```bash
git commit -m "mensaje"
```

### Enviar cambios

```bash
git push origin main
```

## Beneficios del versionamiento
- Historial de cambios
- Trabajo colaborativo
- Recuperación de versiones
- Integración con CI/CD

---

# 8. Conclusiones

Durante el desarrollo del proyecto se implementaron prácticas fundamentales de DevOps utilizando herramientas modernas de automatización, contenerización, monitoreo y control de calidad.

La integración de Docker, GitHub Actions, pruebas automatizadas y métricas permitió construir una aplicación más confiable, reproducible y preparada para despliegues automatizados.

Además, el proyecto permitió comprender la importancia de la integración continua, observabilidad y automatización dentro del ciclo de vida del software.

