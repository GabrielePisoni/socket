import socket
import json

SERVER_IP = "127.0.0.1"
SERVER_PORT = 5005
BUFFER_SIZE = 1024
NUM_MESSAGES = 5

#Creazione del socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

for i in range(NUM_MESSAGES):
  #invio del messaggio al server
  primoNumero=float(input("inserisci il primo numero: "))
  secondoNumero=float(input("inserisci il secondo numero: "))
  operazione=input("inserisci l'operazione (+,-,*,/,%): ")
  message={'primoNumero':primoNumero,
             'operazione':operazione,
             'secondoNumero': secondoNumero}
  message = json.dumps(message) # Trasformiamo l'oggetto in una stringa
  sock.sendto(message.encode("UTF-8"), (SERVER_IP, SERVER_PORT))

  data, addr = sock.recvfrom(BUFFER_SIZE)
  print("Risultato: ", data.decode())
 
  sock.sendto(message.encode(), (SERVER_IP, SERVER_PORT))
  print(f"Messaggio inviato al server: {message}")

  #ricezione della risposta dal server
  data, addr = sock.recvfrom(BUFFER_SIZE)
  print(f"Messaggio ricevuto dal server {addr}: {data.decode()} {type(data.decode())} ")

#Chiusura del socket
sock.close()