#🧟‍♂️Mobs de Minecraft en Python

Este proyecto simula distintos **mobs** inspirados en Minecraft. Cada mob tiene **nombre, nivel, sonido y comportamiento**, y puede presentarse mostrando su información en consola.

---

## 🎯 Qué hace

* Crear mobs como `Vaca`, `Creeper`, `Enderman` y `Zombie`
* Mostrar el sonido característico de cada mob
* Mostrar su comportamiento y forma de moverse
* Simular un pequeño “encuentro con mobs” en consola

---

## ▶ Cómo usarlo

```python id="mobs_example"
from vaca import Vaca
from creeper import Creeper
from enderman import Enderman
from zombie import Zombie

vaca = Vaca("Vaca", 15)
vaca.presentarse()

creeper = Creeper("Creeper", 25)
creeper.presentarse()

enderman = Enderman("Enderman", 40)
enderman.presentarse()

zombie = Zombie("Zombie", 35)
zombie.presentarse()
```

---

## 💡 Ejemplo de salida

```text id="mobs_output"
Hola, soy Vaca, nivel 15, y hago Muuu
Hola, soy Creeper, nivel 25, cuidado con la explosión
Hola, soy Enderman, nivel 40, me teletransporto
Hola, soy Zombie, nivel 35, camino lentamente y busco jugadores
```

---

## 📈 Posibles mejoras

* Agregar más mobs y comportamientos especiales
* Implementar interacción entre mobs y jugador
* Crear un sistema de combate o eventos
* Añadir interfaz gráfica tipo juego

---

## 🛠 Requisitos

* Python 3.x
