logs = [
    ("192.168.1.1", "/home", "Chrome"),
    ("192.168.1.2", "/login", "Firefox"),
    ("192.168.1.1", "/dashboard", "Chrome"),
    ("192.168.1.3", "/home", "Edge"),
    ("192.168.1.2", "/home", "Firefox")
]

ip_url = {}         
visitas_url = {}    
navegadores = {}    
ips = set()         

for linea in logs:
    ip = linea[0]
    url = linea[1]
    navegador = linea[2]
    
    if ip not in ip_url:
        ip_url[ip] = set()
    ip_url[ip].add(url)
    
    if url not in visitas_url:
        visitas_url[url] = 0
    visitas_url[url] = visitas_url[url] + 1
    
    if navegador not in navegadores:
        navegadores[navegador] = 0
    navegadores[navegador] = navegadores[navegador] + 1

    ips.add(ip)

print(f"URLs por IP: {ip_url}")
print(f"Visitas totales: {visitas_url}")
print(f"IPs únicas: {sorted(ips)}") 

mayor = 0
mas_usado = ""

for nav in navegadores:
    cantidad = navegadores[nav]
    if cantidad > mayor:
        mayor = cantidad
        mas_usado = nav

print(f"El navegador ganador es: {mas_usado}")