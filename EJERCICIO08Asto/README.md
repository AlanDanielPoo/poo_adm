🎮 Torneo de Videojuegos TecNM

Sistema básico en Python para simular la gestión de participantes en un torneo de videojuegos del Tecnológico Nacional de México (TecNM).

Este proyecto modela dos tipos de usuarios dentro del torneo:

🏆 Competidores
👀 Observadores
📌 Descripción

El programa permite crear y gestionar perfiles de participantes dentro de un torneo, donde:

Los competidores pueden acumular o perder puntos según su desempeño.
Los observadores pueden visualizar partidas y llevar un registro de cuántas han visto.

Este sistema es una simulación sencilla pensada como práctica de programación orientada a objetos.

📂 Estructura del Proyecto
.
├── main.py
├── competidor.py
└── observador.py
🚀 Ejecución

Ejecuta el programa con:

python main.py
🧠 Funcionalidades
🏆 Competidor

Representa a un jugador inscrito en el torneo TecNM.

Características:

Registro con nombre, número de control, nivel y equipo
Visualización de perfil
Sistema de puntos:
➕ Ganar puntos por victorias
➖ Perder puntos por derrotas
👀 Observador

Representa a asistentes o espectadores del torneo.

Características:

Registro con nombre, número de control y nivel
Visualización de partidas
Contador de partidas observadas
Mostrar perfil
📋 Ejemplo de Simulación

El programa realiza lo siguiente:

🎮 Se registra un competidor del TecNM:
Nombre: Alan Astorga
Equipo: AstoMx
📊 Se muestran sus datos y se ajustan sus puntos
👀 Se registra una observadora:
Nombre: Maria Fernanda
🎥 Observa dos partidas del torneo
📄 Se muestra su perfil actualizado
🛠️ Requisitos
Python 3.x
🎯 Objetivo Académico

Este proyecto forma parte de una práctica para reforzar conceptos como:

Programación Orientada a Objetos (POO)
Uso de clases y métodos
Modularización del código
🚧 Posibles Mejoras
🏅 Sistema de rankings del torneo
💾 Guardado de datos en archivos o base de datos
🌐 Interfaz web o gráfica
🎮 Soporte para múltiples juegos
