# Simulación de Herramientas tipo Minecraft

Este proyecto simula el uso de herramientas en un juego estilo **Minecraft**, mostrando cómo diferentes herramientas interactúan con distintos objetivos y cómo se desgastan hasta romperse.

---

## 📂 Estructura del proyecto

```
proyecto-herramientas/
│
├── pico.py       # Clase Pico
├── espada.py     # Clase Espada
├── pala.py       # Clase Pala
├── arco.py       # Clase Arco
├── main.py       # Script principal que ejecuta la simulación
└── README.md     # Documentación del proyecto
```

---

## 🛠️ Clases y Herramientas

* **Pico**: Usado para extraer minerales (Ej: Mena de diamante).
* **Espada**: Usada para combatir enemigos (Ej: Zombies, Esqueletos).
* **Pala**: Usada para remover bloques como arena.
* **Arco**: Permite atacar enemigos a distancia con flechas.

Cada herramienta tiene:

* **Material**: Oro, Hierro, Piedra, Diamante, etc.
* **Nivel de eficiencia**: Determina velocidad o daño.
* **Durabilidad**: Se reduce con cada uso hasta romperse.

---

## ⚡ Cómo ejecutar

1. Clona el repositorio:

```bash
git clone https://github.com/tuusuario/proyecto-herramientas.git
```

2. Ingresa a la carpeta del proyecto:

```bash
cd proyecto-herramientas
```

3. Ejecuta el script principal:

```bash
python main.py
```

Esto generará una simulación donde cada herramienta interactúa con un objetivo hasta que se rompa.

---

## 📝 Ejemplo de salida

```
Usando Pico de Oro en Mena de diamante
Extraí algo de Mena de diamante
Durabilidad restante: 1

Usando Espada de Diamante en Zombie
Atacaste al Zombie
Durabilidad restante: 1

Usando Pala de Hierro en Arena
Removiste Arena
Durabilidad restante: 1

Usando Arco de Piedra en Esqueleto
Disparaste una flecha al Esqueleto
Flechas restantes: 9
Durabilidad restante: 2
```

---

## 💡 Mejoras futuras

* Añadir más herramientas y materiales.
* Implementar efectos especiales según el objetivo.
* Agregar gestión de inventario y recolección de recursos.
* Soporte multijugador o simulación de combate completo.
