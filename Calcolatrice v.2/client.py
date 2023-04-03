# Client
import socket
import json

HOST = '127.0.0.1' # Indirizzo del server
PORT = 65432       #Porta usata dal server
BUFFER_SIZE = 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock_service:

  primoNumero=float(input("inserisci il primo numero: "))
  secondoNumero=float(input("inserisci il secondo numero: "))
  operazione=input("inserisci l'operazione (+,-,*,/,%): ")
  message={'primoNumero':primoNumero,
             'operazione':operazione,
             'secondoNumero': secondoNumero}
  
  message = json.dumps(message) # Trasformiamo l'oggetto in una stringa
  sock_service.connect((HOST, PORT))
 
  sock_service.sendall(message.encode())  # invio direttamente in formato byte
  data = sock_service.recv(1024) # il parametro indica la dimensione massima dei dati che possono essere ricevuti in una sol a volta


#a questo punto la socket è stata chiusa automaticamente
print('Received', data.decode())