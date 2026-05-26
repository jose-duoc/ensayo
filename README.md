Para presentar ambos archivos como un único proyecto en GitHub, lo ideal es crear un README.md unificado que explique que el repositorio es una "Suite de Gestión Logística" o "Sistema de Operaciones".

Aquí tienes la propuesta del README.md que integra ambos sistemas (Bicicletas + Equipaje):

🛫 Sistema de Gestión Logística - Operaciones Combinadas
Este repositorio contiene un conjunto de herramientas desarrolladas en Python para la automatización de procesos logísticos. El proyecto se divide en dos módulos principales: Gestión de Transporte Urbano (Bicicletas) y Registro de Carga Aérea (VuelosChile).

📁 Estructura del Proyecto
El proyecto consta de los siguientes módulos independientes:

gestion_bicis.py: Sistema de control de inventario y arriendo de bicicletas.

registro_equipaje.py: Validador y clasificador de equipaje para aerolíneas.

🚲 1. Sistema de Gestión de Bicicletas
Diseñado para administrar una estación de bicicletas con capacidad limitada, controlando el flujo de usuarios.

Características:
Control de Stock: Monitoreo en tiempo real de 25 unidades.

Validación de Capacidad: Evita la devolución de unidades si la estación está llena.

Historial: Seguimiento de viajes activos en el momento.

✈️ 2. Registro de Equipaje - VuelosChile
Script automatizado para clasificar maletas entre cabina y bodega basándose en reglas de peso y seguridad de tickets.

Características:
Seguridad de Ticket: Valida códigos de ticket (mín. 5 caracteres, sin espacios).

Clasificación Automática: * 🧳 Cabina: ≤ 10 kg.

📦 Bodega: > 10 kg.

Manifiesto de Carga: Resumen final con el conteo total por categoría.

🛠️ Conceptos de Programación Aplicados
Ambos scripts están construidos bajo estándares de robustez básicos:

Manejo de Excepciones (try-except): Para evitar que el programa falle ante entradas de texto en campos numéricos.

Validación Persistente: Uso de ciclos while para asegurar que el usuario ingrese datos correctos antes de avanzar.

Lógica de Negocio: Estructuras condicionales complejas para la toma de decisiones.

🚀 Instalación y Uso
Clonar el repositorio:

Bash
git clone https://github.com/tu-usuario/logistica-python.git
cd logistica-python
Ejecutar los módulos:

Para gestionar bicicletas:

Bash
python gestion_bicis.py
Para registrar equipaje:

Bash
python registro_equipaje.py
🤝 Contribuciones
¡Las contribuciones son bienvenidas!

Haz un Fork del proyecto.

Crea una rama para tu mejora (git checkout -b feature/NuevaMejora).

Haz un Commit de tus cambios.

Abre un Pull Request.

Desarrollado con fines académicos y de gestión logística.
