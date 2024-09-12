from fastapi import FastAPI
import datetime

app = FastAPI()

app.contador = 0
app.contador_hora = 0

@app.get("/consultas/")
def consultar_consultas(hora: bool = True):
    if hora:
        return f"La fecha (con hora) se consultó {app.contador_hora} veces"
    else:
        return f"La fecha (sin hora) se consultó {app.contador} veces"

@app.post("/")
def consultar_fecha(hora: bool = True):
    ahora = datetime.datetime.now()
    if hora:
        app.contador_hora = app.contador_hora + 1
        return f"{ahora.strftime('%Y-%d-%m %H:%M:%S')}"
    else:
        app.contador = app.contador + 1
        return f"{ahora.strftime('%Y-%d-%m')}"
        
"El metodo POST puede ejecutarse desde una terminal con 'curl -X POST http://localhost:8000/?hora=True'"
"El metodo GET puede ejecutarse desde una terminal con 'curl -X GET http://localhost:8000/consultas/?hora=True'"
