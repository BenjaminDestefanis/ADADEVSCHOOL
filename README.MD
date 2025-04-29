* PLATAFORMA E-LEARNING BASICA Y ESCALABLE 

* *ESTRUCTURA DEL PROYECTO*

1. Visión, Objetivos y Alcance

Visión: Crear un espacio intuitivo y seguro para que instructores publiquen cursos y estudiantes accedan a contenido de calidad, con posibilidad de crecer hacia un marketplace completo y un blog de apoyo.
Objetivos MVP:

- Registro y autenticación de usuarios (estudiantes e instructores).
- Publicación y gestión de cursos básicos (video, PDF, quizzes).
- Sistema de pago sencillo (Stripe/PayPal).
- Dashboard para instructores (subir contenido, ver ventas).
- Dashboard para estudiantes (acceder cursos, progreso).
- Alcance inicial: Funcionalidades mínimas viables para validar el modelo de negocio.

2. Modelo de Negocio

- Fuente de ingreso
- Descripción
- Prioridad MVP
- Venta de cursos
- Comisión por cada venta (10–30%).
- Alta
- Suscripción mensual
- Acceso ilimitado a catálogo (Freemium).
- Media
- Cursos destacados
- Pago adicional para promoción en homepage.
- Baja
- Afiliados / referidos
- Incentivos por traer nuevos alumnos/instructores.
- Baja
- Estrategia de precios: comenzar con precios competitivos y ofertas de lanzamiento.

3. Requerimientos Funcionales y No Funcionales

- Funcionales
- Usuarios: Registro, login, roles (estudiante, instructor, admin).
- Cursos: CRUD de cursos, módulos, lecciones.
- Contenido: Streaming de video, descarga de recursos.
- Pagos: Integración Stripe/PayPal.
- Progreso: Tracking de avance, quizzes básicos.
- Notificaciones: Email de bienvenida, recordatorios.
- No Funcionales
- Escalabilidad: Arquitectura modular, contenedores Docker.
- Seguridad: HTTPS, JWT, validación de inputs.
- Performance: CDN para videos y assets.
- Mantenibilidad: Código limpio, tests unitarios.


6. Diseño UI/UX (Wireframes Iniciales)

Landing Page: CTA claro (registro, catálogo).

Página de Curso: Título, descripción, instructor, precio.

Dashboard Estudiante: Lista de cursos, progreso.

Dashboard Instructor: Gestión de contenido, métricas.

Herramienta sugerida: Figma para prototipado colaborativo.

7. Integración de Blog

Enfoque Headless: Usar Strapi/Ghost para gestionar posts.

Frontend unificado: Consumir API del CMS e integrar estilos.

SEO & Performance: Generar sitemap, SSR con Vite + React.

8. Roadmap de Desarrollo

Fase

Objetivos Principales

Tiempo estimado

1

Setup repos, Docker, registros usuarios, login

1–2 semanas

2

CRUD de cursos, upload video, visualización

2–3 semanas

3

Integración pagos, dashboards básicos

1–2 semanas

4

Tests, CI/CD, deploy en staging

1 semana

5

Integración CMS para blog, SEO básico

1–2 semanas

6

Feedback, mejoras UX, optimización rendimiento

Continuo