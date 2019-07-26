print("Server  en ligne pour la communication")

import mysql.connector  # importation du module MySql
import socket    # importation du module socket
import pickle
import time
	
def serveur():	
	serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Creation du socket serveur 
	serveur.bind(("127.0.0.1",55000)) # creation d'interface de communication en passant par le port 550000
	
	while "true":
		serveur.listen(5) # limite le nombre requettes a 2 seulement
		client, infos = serveur.accept() # accept et attend la connexion du client
		
		while "true":
			msg = client.recv(1024)# le receveur recoit le msg du client et recv n'accept que les premiers 1024 caracteres
			msg = msg.decode()
			msg = msg.split(";") 
			if msg[0] == "1" :
			
				print(">",msg[1])

				bdd = mysql.connector.connect(host="localhost", user="root", passwd="ruffin", db="bdlivre")

				curseur = bdd.cursor()  # il faut creer un objet Curseur pour executer les requettes dont nous avons besoin
				curseur.execute("SELECT * FROM livre where id = '%d' " % int(msg[1]))  # execution des requettes

				for row in curseur:
						data = zip(curseur.description, row)
						
				serialized = pickle.dumps(data) 
				serveur.close()

				serveur1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				serveur1.connect(("127.0.0.1",55001))
				serveur1.sendall(serialized)

				bdd.close()

			elif msg[0] == "2":
			
				bdd = mysql.connector.connect(host="localhost", user="root", passwd="ruffin", db="bdlivre")

				curseur = bdd.cursor()  # il faut creer un objet Curseur pour executer les requettes dont nous avons besoin
				curseur.execute("SELECT id, nom_livre FROM livre")  # execution des requettes
			
				serveur1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				serveur1.connect(("127.0.0.1",55001))
					
				for row in curseur:
						
					serialized = pickle.dumps(row) 
					serveur1.send(serialized)
					time.sleep(1)
					print (row)
					if not(row):
						break

				bdd.close()
serveur()
