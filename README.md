# Página Web — Sitio Web Personal Interactivo

Página Web es un proyecto de sitio web responsivo desarrollado con **HTML**, **CSS** y **JavaScript**, diseñado como una página de demostración y portfolio personal con un enfoque en diseño moderno y usabilidad.

Este proyecto es una plataforma para aprender y practicar desarrollo web frontend, con énfasis en diseño visual, interactividad y buenas prácticas de código.

![status](https://img.shields.io/badge/estado-en%20desarrollo-yellow)
![html5](https://img.shields.io/badge/html5-frontend-orange)
![css3](https://img.shields.io/badge/css3-styling-blue)
![javascript](https://img.shields.io/badge/javascript-interactividad-yellow)
![license](https://img.shields.io/badge/licencia-sin%20especificar-lightgrey)

---

## ✨ Características

- **Diseño responsivo**: Adaptable a todos los tamaños de pantalla (mobile, tablet, desktop)
- **Interfaz moderna**: Utiliza principios de diseño contemporáneo y buena UX
- **Navegación intuitiva**: Menú fluido y fácil acceso a secciones
- **Animaciones suaves**: Transiciones CSS y efectos JavaScript
- **Optimización SEO**: Estructura semántica y meta tags
- **Despliegue en la nube**: Alojado en Render con actualizaciones automáticas
- **Totalmente personalizable**: Fácil de adaptar y extender

## 🧱 Stack técnico

| Componente | Tecnología |
|---|---|
| Markup | HTML5 |
| Estilos | CSS3 (Flexbox, Grid, Animaciones) |
| Interactividad | JavaScript vanilla (ES6+) |
| Alojamiento | Render |
| Control de versiones | Git |
| Plataforma | Web (todos los navegadores modernos) |

## 📂 Estructura del proyecto

```
Pagina_web/
├── index.html             # Página principal
├── pages/                 # Páginas adicionales
│   ├── about.html
│   ├── portfolio.html
│   └── contact.html
├── css/
│   ├── style.css          # Estilos principales
│   ├── responsive.css     # Media queries
│   └── animations.css     # Efectos y transiciones
├── js/
│   ├── script.js          # Lógica principal
│   ├── nav.js             # Navegación interactiva
│   └── forms.js           # Validación de formularios
├── assets/
│   ├── images/            # Imágenes optimizadas
│   ├── icons/             # Iconos SVG
│   └── fonts/             # Tipografías personalizadas
└── README.md
```

## ⚙️ Cómo funciona

```
Usuario accede a la web
        │
        ├─→ HTML renderiza estructura
        │
        ├─→ CSS aplica estilos
        │
        ├─→ JavaScript agrega interactividad
        │
        ├─→ Navegación entre secciones
        │
        ├─→ Formularios validan datos
        │
        └─→ Experiencia fluida y moderna
```

1. **Carga inicial**: El navegador interpreta HTML, CSS y JavaScript
2. **Renderizado**: Se dibuja la interfaz con estilos responsivos
3. **Interactividad**: JavaScript captura eventos del usuario (clicks, scroll, etc.)
4. **Navegación**: Los enlaces permiten moverse entre secciones sin recargar
5. **Validación**: Los formularios validan datos antes de enviar
6. **Animaciones**: Transiciones suaves en elementos e interacciones

## 🚀 Instalación

### Requisitos previos

- **Navegador moderno** (Chrome, Firefox, Safari, Edge)
- **Servidor web local** (opcional, para desarrollo)
- **Git** (para clonar)

### Pasos

1. Clona el repositorio:
   ```bash
   git clone https://github.com/Gal4h4d/Pagina_web.git
   cd Pagina_web
   ```

2. **Opción A - Ejecución directa** (sin servidor):
   - Abre `index.html` directamente en tu navegador
   - Funciona para desarrollo básico

3. **Opción B - Con servidor local** (recomendado):
   ```bash
   # Con Python 3:
   python -m http.server 8000
   
   # O con Node.js (http-server):
   npx http-server
   ```
   - Accede a `http://localhost:8000`

4. **Para ver en producción**:
   - Visita: https://pagiba-web.onrender.com

## 🔧 Configuración / personalización

- **Cambiar colores y tema**: Edita las variables CSS en `css/style.css`:
  ```css
  :root {
    --color-primary: #007bff;
    --color-secondary: #6c757d;
    --font-main: 'Segoe UI', sans-serif;
  }
  ```

- **Agregar nuevas páginas**: Crea un archivo `.html` en `pages/` y añade el enlace en la navegación

- **Personalizar contenido**: Reemplaza textos, imágenes e información en los archivos HTML

- **Agregar formularios**: Modifica `js/forms.js` para manejar envíos a tu backend:
  ```javascript
  const form = document.querySelector('#contact-form');
  form.addEventListener('submit', (e) => {
    e.preventDefault();
    // Lógica de envío
  });
  ```

- **Optimizar imágenes**: Comprime assets en `assets/images/` para mejor rendimiento

- **Cambiar tipografías**: En `css/style.css`, importa nuevas fuentes de Google Fonts

## 📚 Componentes principales

### Header
Barra de navegación principal con menú responsivo y logo del sitio.

### Hero Section
Sección introductoria con imagen de fondo y call-to-action.

### Portfolio
Galería de proyectos o trabajos con animaciones al hacer hover.

### About
Sección "Acerca de mí" con información personal y habilidades.

### Contact
Formulario de contacto con validación cliente-side.

### Footer
Pie de página con enlaces e información de contacto.

## 🧪 Testing

Para verificar que todo funciona:

1. Abre la página en distintos navegadores
2. Verifica responsividad redimensionando la ventana
3. Valida formularios con datos inválidos
4. Comprueba que todos los enlaces funcionan
5. Inspecciona con DevTools (F12) para depurar

## 🗺️ Estado actual y próximos pasos

- [x] Estructura HTML semántica
- [x] Diseño responsivo
- [x] Navegación funcional
- [x] Despliegue en Render
- [ ] Backend para envío de formularios
- [ ] Sistema de comentarios
- [ ] Blog o sección de artículos
- [ ] Galería de imágenes mejorada
- [ ] Integración con redes sociales
- [ ] Análisis de visitantes (Analytics)
- [ ] Modo oscuro/claro toggle
- [ ] Múltiples idiomas (i18n)

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Para contribuir:

1. Fork el repositorio
2. Crea una rama para tu feature (`git checkout -b feature/mi-feature`)
3. Commit tus cambios (`git commit -m 'Agrega mi feature'`)
4. Push a la rama (`git push origin feature/mi-feature`)
5. Abre un Pull Request

## 👤 Autor

**Juan David** ([Gal4h4d](https://github.com/Gal4h4d)) — proyecto personal de exploración de desarrollo web frontend, diseño responsivo y buenas prácticas de HTML/CSS/JavaScript.

---

⭐ Si encontraste útil este proyecto, ¡considera dejarle una estrella en GitHub!
