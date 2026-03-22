# 🐾 Animales con Clases Abstractas en Python

Este proyecto muestra cómo usar **clases abstractas** y **herencia** en Python. Se crea una plantilla `Animal` que obliga a sus clases hijas a implementar el método `hablar()`.

---

## 🎯 Qué hace

* Definir una clase abstracta `Animal` con un método `hablar()`
* Crear clases concretas como `Perro` y `Gato` que implementan `hablar()`
* Mostrar en consola los sonidos de cada animal

---

## ▶ Cómo usarlo

```python id="animal_example"
perro = Perro()
gato = Gato()

print(perro.hablar())  # Guau¡
print(gato.hablar())    # Miau¡
```

---

## 💡 Posibles mejoras

* Agregar más animales y sonidos
* Incluir otros métodos abstractos, como `moverse()` o `comer()`
* Crear una lista de animales y recorrerla mostrando sus comportamientos
* Hacer un mini juego donde los animales interactúen entre sí

---

## 🛠 Requisitos

* Python 3.x
