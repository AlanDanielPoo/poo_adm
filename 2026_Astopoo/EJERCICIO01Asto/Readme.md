# 🎓 Sistema de Estudiantes en Python

Un proyecto en Python que permite crear estudiantes, registrar sus calificaciones y calcular su promedio usando programación orientada a objetos.

---

## 🚀 Funcionalidades

* Crear estudiantes con nombre, edad y carrera
* Agregar calificaciones
* Calcular promedio de calificaciones
* Mostrar información completa del estudiante

---

## ▶ Uso

```python
# Crear estudiantes
estudiante1 = Estudiante("Alan",18,"Ing. en Sistemas")
estudiante2 = Estudiante("Scarlet",25,"Ing. en Industrial")

# Agregar calificaciones
estudiante1.setCalificaciones(100)
estudiante1.setCalificaciones(50)
estudiante1.setCalificaciones(40)

# Mostrar información y promedio
print(estudiante1.mostrarInformacionUsuario())
print(f"Promedio de {estudiante1.getNombre()}: {estudiante1.mostrarPromedio()}")
```

**Ejemplo de salida:**

```
Hola, soy Alan, tengo 18 años y estudio Ing. en Sistemas
Promedio de Alan: 63.33
Promedio de Scarlet: 0
```

---

## 🛠 Requisitos

* Python 3.x

---

## 📈 Mejoras posibles

* Validar que las calificaciones estén entre 0 y 100
* Manejar varias asignaturas
* Guardar y cargar datos desde archivos
