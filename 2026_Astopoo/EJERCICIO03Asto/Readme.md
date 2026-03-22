# 🐾 Mi Mascota Virtual en Python

Este proyecto crea un pequeño sistema de mascotas virtuales donde puedes **alimentarlas, jugar con ellas y ver si están felices**. Cada mascota tiene un **nombre, tipo, edad y nivel de felicidad**, que cambia según tus interacciones.

---

## 🎯 Qué hace

* Crear mascotas con sus características principales
* Alimentar o jugar con ellas para aumentar su felicidad
* Mostrar el estado actual de la mascota
* Saber si la mascota es feliz o no

---

## ▶ Cómo usarlo

1. Crear tus mascotas:

```python
mascota1 = Mascota("Spaiky", "Perro", 3, 50)
mascota2 = Mascota("Pequeñin", "Gato", 2, 80)
```

2. Ver su estado y felicidad:

```python
print(mascota1.mostrarEstado())
print("¿Es feliz?", mascota1.esFeliz())
```

3. Interactuar con ellas:

```python
mascota1.alimentar()
mascota1.jugar()
print(mascota1.mostrarEstado())
```

---

## 💡 Ideas para mejorar

* Añadir más acciones: pasear, dormir, entrenar
* Crear niveles de felicidad o recompensas
* Guardar el progreso de cada mascota en un archivo
* Hacer una pequeña interfaz gráfica para jugar con ellas

---

## 🛠 Requisitos

* Python 3.x
