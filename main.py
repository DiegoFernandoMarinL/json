import json
import requests

#example = [
#    {"nombre":"Diego"},
#    {"nombre":"Fernando"},
#    ["Hola Mundo"]
#]
#example = json.dumps(example,indent=4)

#print(example)
empleadoNuevo = {
    "codigo": 999,
    "nombre": "Andres",
    "apellido": "Lizaraso"
}
obtener = requests.post("http://172.16.100.119:5502", data=json.dumps(empleadoNuevo))
print(obtener)
