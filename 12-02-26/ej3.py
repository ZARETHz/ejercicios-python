config_base = {"host": "localhost", "port": 3306, "debug": False, "log_level": "info"}

config_dev = config_base.copy()
config_dev.update({
    "debug": True,
    "log_level": "verbose"
})

config_prod = config_base.copy()
config_prod.update({
    "host": "192.168.1.10",
    "log_level": "error"
})

def conectar(**kwargs):
    print("Configuración activa:", kwargs)

conectar(**config_dev)