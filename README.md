# GameDex
Gestión de Biblioteca de Videojuegos

**Módulo:** Diseño de Interfaces · 2.º DAM  
**Tecnologías:** Python 3.10+, PySide6, Qt Designer y SQLite.

## 1. Descripción
GameDex es una aplicación de escritorio para catalogar una biblioteca personal de videojuegos. Permite consultar, buscar, filtrar, añadir, editar y eliminar títulos. Los datos se guardan localmente en SQLite.

## 2. Requisitos
- Python 3.10 o superior.
- PySide6.
- Linux, Windows o macOS.

## 3. Instalación y ejecución
Abre una terminal dentro de la carpeta `GameDex` y ejecuta:

```bash
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
# .venv\Scripts\activate    # Windows
pip install -r requirements.txt
python main.py
```

La primera ejecución crea automáticamente `gamedex.db` y añade cuatro registros de ejemplo. Para iniciar la aplicación en otras ocasiones basta con `python main.py`.

## 4. Estructura
```text
GameDex/
├── main.py
├── database.py
├── requirements.txt
├── README.md
├── README.pdf
├── ui/
│   ├── main_window.ui
│   └── game_form.ui
├── components/
│   └── game_card.py
└── resources/
    ├── images/
    └── icons/
```

## 5. Funcionalidades
- Ventana principal con catálogo visual.
- Búsqueda dinámica por título.
- Filtros por género y plataforma.
- Alta y edición con formulario.
- Eliminación con confirmación modal.
- Validación del título obligatorio.
- Base de datos SQLite y creación automática de tabla.
- Componente reutilizable `GameCard`.
- Mensajes de confirmación y error.

## 6. Base de datos
La tabla `videojuegos` contiene:
- `id`: clave primaria autoincremental.
- `titulo`: texto obligatorio.
- `genero`: texto.
- `plataforma`: texto.
- `anio`: entero.
- `puntuacion`: número decimal de 0 a 5.
- `Caratura`: donde se guarda la foto del juego.

## 7. Diseño y accesibilidad
Las interfaces están separadas en archivos `.ui` para poder abrirlas y modificarlas con Qt Designer. Se utilizan layouts, etiquetas descriptivas, contraste elevado, botones con texto y campos de formulario identificados.

## 8. Archivos y mantenimiento
La base de datos se genera en la carpeta del proyecto al ejecutar `main.py`. No se utilizan rutas absolutas para recursos gráficos. Las carpetas `resources/images` y `resources/icons` quedan preparadas para añadir carátulas e iconos propios.

## 9. Integrantes
- Nombre: Kaili

## 10. Comprobación
Desde la carpeta del proyecto:
```bash
python main.py
```

