import eventlet
import socketio
from flask import Flask, render_template, send_from_directory

# Crear una instancia de servidor Socket.IO
sio = socketio.Server(cors_allowed_origins="*")

# Crear una aplicación Flask para integrar Socket.IO
app = Flask(__name__)
app.wsgi_app = socketio.WSGIApp(sio, app.wsgi_app)

# Ruta para servir el archivo HTML
@app.route("/")
def index():
    return send_from_directory(".", "index.html")

# Evento: conexión de un cliente
@sio.event
def connect(sid, environ):
    print(f"Cliente conectado: {sid}")

# Evento: mensaje personalizado
@sio.event
def mensaje(sid, data):
    print(f"Mensaje recibido de {sid}: {data}")
    sio.emit('respuesta', f"Hola, {data}!", to=sid)

# Evento: desconexión de un cliente
@sio.event
def disconnect(sid):
    print(f"Cliente desconectado: {sid}")

# Iniciar el servidor usando eventlet
if __name__ == "__main__":
    eventlet.wsgi.server(eventlet.listen(("0.0.0.0", 5000)), app)