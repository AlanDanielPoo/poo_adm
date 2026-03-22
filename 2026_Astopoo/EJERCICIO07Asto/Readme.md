# Proyecto: Manejo de Excepciones en Python

Este proyecto es un ejemplo práctico para aprender **manejo de errores en Python** usando `try`, `except`, `else` y `finally`. Permite al usuario realizar operaciones seguras, detectando errores comunes como división por cero o entradas inválidas.

---

## 📂 Estructura del proyecto

```text
manejo-excepciones/
│
├── main.py       # Script principal con ejemplos de manejo de excepciones
└── README.md     # Documentación del proyecto
```

---

## ⚡ Objetivos del proyecto

* Enseñar a capturar errores con `try / except`.
* Mostrar cómo usar `else` y `finally` para un flujo controlado.
* Prevenir que el programa se detenga por errores comunes.
* Dar mensajes claros al usuario cuando ocurre un error.

---

## 📝 Ejemplo de código

```python
try:
    a = int(input("Ingresa el numerador: "))
    b = int(input("Ingresa el denominador: "))
    total = a / b
except ValueError:
    print("Error: Debes ingresar un número entero, no una letra.")
except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")
else:
    print(f"El resultado de {a} / {b} es {total}")
finally:
    print("¡Gracias por usar el programa de división!")
```

---

## 🔹 Explicación de cada bloque

| Bloque    | Función                                                   |
| --------- | --------------------------------------------------------- |
| `try`     | Código que podría generar errores.                        |
| `except`  | Captura errores específicos y ejecuta código alternativo. |
| `else`    | Se ejecuta si **no hubo errores** en el `try`.            |
| `finally` | Se ejecuta **siempre**, sin importar si hubo error o no.  |

---

## 💡 Mejoras posibles

* Agregar **bucle de reintento** para que el usuario intente nuevamente si ingresa datos inválidos.
* Manejar más tipos de errores (Ej: Overflow, KeyboardInterrupt).
* Extender el programa para operaciones matemáticas adicionales (suma, resta, multiplicación).
* Guardar un historial de operaciones y errores en un archivo de registro (`log`).

---

## 🏃 Cómo ejecutar

1. Clona el repositorio:

```bash
git clone https://github.com/tuusuario/manejo-excepciones.git
```

2. Entra a la carpeta:

```bash
cd manejo-excepciones
```

3. Ejecuta el script:

```bash
python main.py
```

4. Ingresa los números cuando se te solicite y observa cómo el programa maneja errores automáticamente.

---

## 📌 Ejemplo de salida

```text
==================================================
PARTE 1: División con manejo de errores
==================================================
Ingresa el numerador: 10
Ingresa el denominador: 0
Error: No se puede dividir por cero.
¡Gracias por usar el programa de división!
```

```text
Ingresa el numerador: 8
Ingresa el denominador: 2
El resultado de 8 / 2 es 4.0
¡Gracias por usar el programa de división!
