inventario = [
    {"producto": "Laptop", "categoria": "Electrónica", "stock": 5},
    {"producto": "Mouse", "categoria": "Electrónica", "stock": 25},
    {"producto": "Silla", "categoria": "Muebles", "stock": 2},
    {"producto": "Escritorio", "categoria": "Muebles", "stock": 0}
]

categoria_producto = {}
agotados = set()
bajo_stock = []

for item in inventario:
    cat = item["categoria"]
    prod = item["producto"]
    stock = item["stock"]
    
    if cat not in categoria_producto:
        categoria_producto[cat] = []
    categoria_producto[cat].append(prod)
    
    if stock == 0:
        agotados.add(prod)
        
    if stock < 5:
        bajo_stock.append(prod)

print(f"Diccionario de productos por categoria:\n {categoria_producto}")
print(f"Tus productos agotados son:\n {agotados}")
print(f"Tus productos con stock menor a 5 son: \n {tuple(bajo_stock)}")

total = {}
for cat in categoria_producto:
    cantidad = len(categoria_producto[cat])
    total[cat] = cantidad

print(f"Total de productos por categoria:\n {total}")