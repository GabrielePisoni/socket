# Server 
import socket
import json

# Configurazione del server 
IP="127.0.0.1"
PORTA = 65432
DIM_BUFFER = 1024

#Creazione della socket del server con il costrutto with
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock_server:

  #Binding della socket alla porta specificata
  sock_server.bind((IP, PORTA))

  #Metti la socket in ascolto per le connessioni in ingresso 
  sock_server.listen()

  print(f"Server in ascolto su {IP}:{PORTA}...")

  #Loop principale del server
  while True:
    #accetta le connessioni
    sock_service, address_client = sock_server.accept() 
    with sock_service as sock_client:

      #Leggi i dati inviati dal client
      data = sock_client.recv(DIM_BUFFER)
      if not data:
        break
      data = data.decode()
      data = json.loads(data)
      primoNumero=data['primoNumero']
      operazione=data['operazione']
      secondoNumero=data['secondoNumero']

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

      # Stampa il messaggio ricevuto e invia una risposta al client 
      print(f"Ricevuto messaggio dal client {sock_client}: {data}") 
      sock_client.sendall(str(reply).encode())