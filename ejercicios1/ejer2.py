asistencias = [
    ("Matemáticas", "Juan", "2024-09-01"),
    ("Matemáticas", "Ana", "2024-09-01"),
    ("Física", "Juan", "2024-09-01"),
    ("Matemáticas", "Juan", "2024-09-02"),
    ("Física", "Ana", "2024-09-02")
]

informe = {}       
dias_alumno = {}    

for asignatura, alumno, fecha in asistencias:
    
    if asignatura not in informe:
        informe[asignatura] = set()
    informe[asignatura].add(alumno)
    if alumno not in dias_alumno:
        dias_alumno[alumno] = set()
    dias_alumno[alumno].add(fecha)

print(f"Informe por materia:\n {informe}")
print(f"Días por alumno:\n {dias_alumno}")

mejor_alumno = ""
mayor_cantidad = 0

for alumno in dias_alumno:
    cantidad = len(dias_alumno[alumno])
    if cantidad > mayor_cantidad:
        mayor_cantidad = cantidad
        mejor_alumno = alumno

print(f"El mejor alumno fue: {mejor_alumno} con {mayor_cantidad} asistencias")