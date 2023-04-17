#calcoServerMultiThread.py
import socket
from threading import Thread
import json

"""
L'interazione tra server, client e socket avviene in questo modo:
Ilserver riceve una richiesta dal client
Il server genera un thread per soddisfare la richiesta su una nuova porta per potersi mettere in attesa di altre richieste
Alla ricezione di una nuova richiesta genera un nuovo thread su una nuova porta e cosi via
"""

SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 22225

def ricevi_comandi(sock_service, addr_client):
  print("avviato")
  while True:
    data = sock_service.recv(1024)
    if not data: #se data è vuoto esce dal ciclo
      break
    data=data.decode()
    data=json.loads(data)
    primoNumero=data['primoNumero']
    operazione=data['operazione']
    secondoNumero=data['secondoNumero']
    ris=""
    if operazione=="+":
      ris=primoNumero+secondoNumero
    elif operazione=="-":
      ris=primoNumero-secondoNumero
    elif operazione=="*":
      ris=primoNumero+secondoNumero
    elif operazione=="/":
      if secondoNumero==0:
        ris="non puoi dividere per 0"
      else:
        ris=primoNumero/secondoNumero
    elif operazione=="%":
      ris=primoNumero%secondoNumero
    else:
      ris="Operazione non riconosciuta"
    ris=str(ris)#casting
    sock_service.sendall(ris.encode("UTF-8")) #manda vettore al client

  sock_service.close()

def ricevi_connessioni(sock_listen):
  while True:
    sock_service, addr_client = sock_listen.accept()
    print("\nConnessione ricevuta da "+str(addr_client))
    print("\nCreo un thread per servire le richieste porta di servizio: ")
    try:
      Thread(target=ricevi_comandi, args=(sock_service, addr_client)).start()
    except:
      print("il thread non si avvia")
      sock_listen.close()

def avvia_server(indirizzo, porta):
  sock_listen = socket.socket()
  sock_listen.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  sock_listen.bind((SERVER_ADDRESS, SERVER_PORT))
  sock_listen.listen(5)
  print("Server in ascolto su %s." % str((SERVER_ADDRESS, SERVER_PORT)))
  ricevi_connessioni(sock_listen)

if __name__=='__main__':
  avvia_server(SERVER_ADDRESS, SERVER_PORT)

"""
La funzione avvia_server crea un endpoint di ascolto (sock_listen) dal quale accettare in entrata
la socket di ascolto viene passata alla funzione ricevi_connessioni la quale accetta richieste di connessione
e per ogni richiesta di connessione crea una socket per i dati (sock_service) e un thread per gestire le richeiste
e inviare le risposte
"""