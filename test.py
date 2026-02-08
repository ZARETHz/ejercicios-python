ventas = [
    ("Ana", "Enero", "Laptop", 2, 15000),
    ("Luis", "Enero", "Mouse", 10, 250),
    ("Ana", "Febrero", "Laptop", 1, 15000),
    ("Luis", "Febrero", "Teclado", 5, 800),
    ("Ana", "Enero", "Mouse", 3, 250)
]

ingreso_empleado = {}
ingreso_mes = {}

for emp, mes, _, cant, precio in ventas:
    ingreso = cant * precio
    ingreso_empleado[emp] = ingreso_empleado.get(emp, 0) + ingreso
    ingreso_mes[mes] = ingreso_mes.get(mes, 0) + ingreso
    
print(f"Ingresos por empleado:\n {ingreso_empleado}")
print(f"Tus ingresos por mes son: {ingreso_mes}")

productos = {venta[2] for venta in ventas}
print(f"Conjunto de productos vendidos: {productos}")

mejor_empleado = max(ingreso_empleado, key=ingreso_empleado.get)
print(f"El mejor empleado es: {mejor_empleado}")