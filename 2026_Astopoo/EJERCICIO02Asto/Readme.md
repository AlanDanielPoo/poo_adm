# 🏦 Sistema de Cuenta Bancaria (Python)

Este proyecto en Python permite crear cuentas bancarias, realizar depósitos, retiros y consultar el saldo utilizando programación orientada a objetos.

---

## 🚀 Funcionalidades

* Crear cuentas con titular, número de cuenta y saldo inicial
* Depositar dinero y actualizar el saldo
* Retirar dinero validando que haya suficiente saldo
* Consultar el saldo actual
* Mostrar información del titular y su saldo

---

## ▶ Uso

```python id="bank_example"
cuenta1 = CuentaBancaria("Astorga", "001234567", 4000.0)

print(cuenta1.mostrarInformacion())

cuenta1.depositar(500.0)
print(cuenta1.mostrarInformacion())

print(cuenta1.retirar(1500))
print(cuenta1.mostrarInformacion())
```

**Ejemplo de salida:**

```
Astorga tienes 4000.0
Astorga tienes 4500.0
1500
Astorga tienes 3000.0
```

---

## 🛠 Requisitos

* Python 3.x

---

## 📈 Mejoras posibles

* Validar que los depósitos y retiros sean números positivos
* Registrar un historial de transacciones
* Implementar interés o comisiones
* Crear una interfaz gráfica sencilla para el usuario
