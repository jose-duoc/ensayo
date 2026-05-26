Registro de Equipaje - VuelosChile ✈️
Este es un script de Python diseñado para automatizar y validar el proceso de registro de equipaje para la aerolínea VuelosChile. El sistema permite clasificar las maletas de forma eficiente entre cabina y bodega basándose en reglas de peso y validación de tickets.

🚀 Funcionalidades
Validación de Entrada: Asegura que la cantidad de equipajes y el peso sean valores numéricos positivos.

Seguridad de Ticket: Verifica que el código del ticket sea válido (mínimo 5 caracteres y sin espacios en blanco).

Clasificación Automática: * 🧳 Cabina: Equipajes con un peso menor o igual a 10 kg.

📦 Bodega: Equipajes con un peso superior a 10 kg.

Resumen de Carga: Genera un manifiesto final con el conteo total por categoría.

🛠️ Requisitos
Python 3.x instalado en tu sistema.

📦 Instalación y Uso
Clona este repositorio:

Bash
git clone https://github.com/tu-usuario/vueloschile-registro.git
Navega al directorio del proyecto:

Bash
cd vueloschile-registro
Ejecuta el script:

Bash
python nombre_del_archivo.py
📝 Ejemplo de Flujo
Al ejecutar el programa, el flujo de interacción será el siguiente:

El sistema solicita el total de maletas a procesar.

Por cada maleta, se pide:

Código de ticket: Debe ser mayor a 5 caracteres (ej. TK12345).

Peso (KG): Valor entero positivo.

El sistema indica en tiempo real la clasificación.

Al finalizar, se muestra el Manifiesto de Carga con los totales.

💻 Estructura del Código
El script utiliza conceptos fundamentales de programación:

Ciclos while: Para validaciones de datos persistentes.

Manejo de Excepciones (try-except): Para evitar errores críticos al ingresar texto en campos numéricos.

Estructuras Condicionales: Para la lógica de negocio (clasificación de peso).

🤝 Contribuciones
¡Las contribuciones son bienvenidas! Si tienes ideas para mejorar la validación o añadir nuevas categorías de equipaje:

Haz un Fork del proyecto.

Crea una rama para tu mejora (git checkout -b feature/NuevaMejora).

Haz un Commit de tus cambios (git commit -m 'Añade nueva funcionalidad').

Haz un Push a la rama (git push origin feature/NuevaMejora).

Abre un Pull Request.

Desarrollado para fines académicos y de gestión logística en VuelosChile.
