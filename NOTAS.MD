
# Arquitectura del proyecto

[Frontend] <--> [API Gateway] <--> [Backend Monolito Modular] <--> [Base de Datos]
                                   ↳ [Servicio de Pagos]
                                   ↳ [Servicio de Emails]
                                   ↳ [CMS Headless (blog)]


MVP: Monolito modular en contenedor.
Futura escalabilidad: Extraer servicios (microservicios) según demanda.

5. Stack Tecnológico Recomendado

Capa    Tecnología / Herramienta

Justificación

Frontend

React + Vite + Tailwind CSS

Velocidad de desarrollo, componentes reutilizables.

Backend

Node.js + Express (TypeScript)

Ecosistema rico, escalable, typing seguro.

Base Datos

PostgreSQL

Relacional, sólido para transacciones.

Almacenamiento

AWS S3 o DigitalOcean Spaces

CDN de archivos estáticos y videos.

Autenticación

Auth0 o JWT propio

Seguridad y escalabilidad.

Pagos

Stripe/PayPal SDK

Integración simple y confiable.

Contenedores

Docker + Docker Compose

Despliegue coherente en local y producción.

CI/CD

GitHub Actions

Automatización tests y despliegue.

Infraestructura

DigitalOcean / AWS EC2 + RDS

Coste inicial bajo, crecimiento flexible.

CMS (blog)

Strapi o Ghost (Headless)

Gestión de contenido separada, API-friendly.



# Manejo de DOCKER

- Construccion de imagen

```terminal  
// Construccion de imagen
docker-compose build 
// Inicio del contenedor
docker-compose up