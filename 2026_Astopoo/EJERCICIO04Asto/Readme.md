# 🍴 Menú Interactivo en Python

Este proyecto crea un pequeño sistema de menú en Python donde puedes **registrar y mostrar distintos productos**: comida, bebida y postre, junto con su información y tipo.

---

## 🎯 Qué hace

* Crear productos de tipo `Comida`, `Bebida` y `Postre`
* Mostrar información de cada producto: nombre, precio y categoría
* Identificar el tipo de producto (plato principal, bebida fría, postre, etc.)
* Simular un pequeño menú interactivo en consola

---

## ▶ Cómo usarlo

1. Crear tus productos:

```python id="menu_example"
comida = Comida("Espaguetti", 100.0, "principal")
bebida = Bebida("Soda", 35.0, "Fria")
postre = Postre("Pastel de chocolate", 45.0, False)
```

2. Mostrar la información de cada producto:

```python id="menu_use"
comida.mostrar_info()
comida.tipo()

bebida.mostrar_info()
bebida.tipo()

postre.mostrar_info()
postre.tipo()
```

3. Ejemplo de salida:

```
Nombre: Espaguetti
Precio: $100.0
Categoría: principal
Tipo: Comida
---
Nombre: Soda
Precio: $35.0
Categoría: Fria
Tipo: Bebida
---
Nombre: Pastel de chocolate
Precio: $45.0
Azúcar: No
Tipo: Postre
```

---

## 💡 Posibles mejoras

* Añadir más tipos de productos y categorías
* Permitir registrar varios productos y mostrarlos en un listado
* Implementar precios con descuentos o promociones
* Crear una interfaz gráfica para seleccionar productos

---

## 🛠 Requisitos

* Python 3.x
