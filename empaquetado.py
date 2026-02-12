datos = [1,2,3,4,5]
print(f"Datos originales: {datos}")

copia_datos = datos.copy()
print(f"Copia de datos: {copia_datos}")
copia_datos.append(6)
print(f"Copia de datos después de modificar: {copia_datos}")


def impresion_nombres(*nombres):
    
    print(f"Nombres recibidos: ", *nombres)
    
impresion_nombres("Ana", "Luis", "Carlos")

def impresion_datos(**data):
    print(f"Datos recibidos: {data}")
    
impresion_datos(nombre="Zareth", edad=25)

diccionario_datos = {"marca": "Toyota",
                     "modelo": "Corolla", 
                     "año": 2020}
copia_diccionario = {**diccionario_datos}
impresion_datos(**copia_diccionario)
