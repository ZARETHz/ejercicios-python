estudiantes = [ 
    ("Ana", 85, 90, 78, 92), 
    ("Luis", 88, 76, 95), 
    ("Carlos", 100, 98), 
    ("María", 70, 80, 75, 85, 90) 
]

resultados = {}

for estudiante in estudiantes:
    nombre, *calificaciones = estudiante
    
    promedio = sum(calificaciones) / len(calificaciones)
    mayor = max(calificaciones)
    menor = min(calificaciones)
    
    resultados[nombre] = {
        "promedio": promedio,
        "max": mayor,
        "min": menor,
    }


for nombre, datos in resultados.items():
    print(f"Estudiante: {nombre}")
    print(f"  Promedio: {datos['promedio']:.2f}")
    print(f"  Nota más alta: {datos['max']}")
    print(f"  Nota más baja: {datos['min']}")
    
