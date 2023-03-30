import socket
import json

SERVER_IP = "127.0.0.1"
SERVER_PORT = 5005
BUFFER_SIZE = 1024

#creazione del socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((SERVER_IP, SERVER_PORT))

print("Server in attesa di messaggi...")

while True:
    #Ricezione dei dati dal client
    data, addr = sock.recvfrom(BUFFER_SIZE)
    print(f"Messaggio ricevuto dal client {addr}: {data.decode()}")
    
    # if len(data)==0:
    if not data:
        break
    data = data.decode()
    data = json.loads(data)
    primoNumero=data['primoNumero']
    operazione=data['operazione']
    secondoNumero=data['secondoNumero']

    #invio di una risposta al client
    if (operazione == '+'):
        reply = primoNumero + secondoNumero
    elif (operazione == '-'):
        reply = primoNumero - secondoNumero
    elif (operazione == '*'):
        reply = primoNumero * secondoNumero
    elif (operazione == '/'):
        reply = primoNumero / secondoNumero
    elif (operazione == '%'):
        reply = primoNumero % secondoNumero 
    print(str(reply).encode())
    sock.sendto(str(reply).encode(), addr)