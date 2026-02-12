transacciones = [
    ("2024-01-10", "Ana", "deposito", 5000, "MXN"),
    ("2024-01-12", "Luis", "retiro", 1500, "MXN"),
    ("2024-01-15", "Ana", "retiro", 2000, "MXN"),
    ("2024-01-18", "Carlos", "deposito", 7000, "MXN")
]

balances = {}

for fecha, cliente, tipo, monto, moneda in transacciones:
    balances[cliente] = balances.get(cliente, 0)

    if tipo == "deposito":
        balances[cliente] += monto
    elif tipo == "retiro":
        balances[cliente] -= monto

cliente_mayor = max(balances, key=balances.get)
mayor = balances[cliente_mayor]

print("balances por cliente:")

for cliente, saldo in balances.items():
    print(f"Cliente: {cliente}")
    print(f"  Saldo actual: ${saldo:} MXN")

print("cliente con mayor balance:")
print(f"{cliente_mayor} con ${mayor:} MXN")
