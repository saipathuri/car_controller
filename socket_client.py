import socketio

# standard Python
sio = socketio.Client()

def setup():
    sio.connect('http://raspberrypi:5000')

def send_action(action, value):
    sio.emit('action', {'direction': action, 'value' : value})

def disconnect():
    sio.disconnect()