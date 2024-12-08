import socketio
import threading

# Crear una instancia del cliente Socket.IO
sio = socketio.Client()

# Evento: conexión al servidor
@sio.event
def connect():
    print("Conectado al servidor")

# Evento: recibir respuesta del servidor
@sio.on('respuesta')
def on_respuesta(data):
    print(f"Servidor: {data}")

# Evento: desconexión del servidor
@sio.event
def disconnect():
    print("Desconectado del servidor")

# Bucle para enviar mensajes al servidor
def enviar_mensajes_cliente():
    while True:
        mensaje = input("Escribe un mensaje para el servidor (o 'salir' para desconectar): ")
        if mensaje.lower() == "salir":
            sio.disconnect()
            break
        sio.emit("mensaje", mensaje)

if __name__ == "__main__":
    try:
        # Conecta al servidor
        sio.connect("http://localhost:5000")

        # Ejecutar el bucle de envío de mensajes en un hilo separado
        threading.Thread(target=enviar_mensajes_cliente, daemon=True).start()

        # Mantener la conexión para recibir mensajes
        sio.wait()

    except Exception as e:
        print(f"Ocurrió un error: {e}")
