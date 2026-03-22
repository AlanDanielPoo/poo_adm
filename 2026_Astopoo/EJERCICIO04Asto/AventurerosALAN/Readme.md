# Aventureros de la Taberna

Este proyecto simula un pequeño juego de personajes donde puedes crear distintos héroes y ver sus habilidades especiales en acción. Cada personaje tiene **nombre, nivel y habilidad** única.

---

## 🎯 Qué hace

* Crear personajes: `Guerrero`, `Mago` y `Arquero`
* Mostrar información del personaje
* Usar su habilidad especial
* Simular ataques y habilidades en consola

---

## ▶ Cómo usarlo

1. Crear tus héroes:

```python id="rpg_example"
guerrero = Guerrero("Daniel", 25, "Hacha")
mago = Mago("Galan", 18, "Bola de fuego")
arquero = Arquero("Scream", 15, 40)
```

2. Presentarlos y usar sus habilidades:

```python id="rpg_use"
guerrero.presentarse()
guerrero.usar_habilidad()

mago.presentarse()
mago.usar_habilidad()

arquero.presentarse()
arquero.usar_habilidad()
```

3. Salida esperada:

```text id="rpg_output"
Hola, soy Daniel, nivel 25, y estoy listo para pelear con mi Hacha
¡Ataque poderoso con Hacha!
Habilidad de combate

Hola, soy Galan, nivel 18, y lanzo mi hechizo: Bola de fuego
¡Bola de fuego lanzada!
Habilidad de hechizo

Hola, soy Scream, nivel 15, y disparo a distancia con precisión 40
¡Ataque a distancia realizado!
Habilidad a distancia
```

---

## 💡 Posibles mejoras

* Agregar más clases de personajes (Hechicero, Tanque, Asesino…)
* Implementar puntos de vida y daño
* Crear un sistema de combate entre personajes
* Guardar estadísticas y niveles de cada héroe

---

## 🛠 Requisitos

* Python 3.x
