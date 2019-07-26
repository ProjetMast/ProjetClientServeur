import socket    # importation du module socket
import pickle

def client() :
	
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Creation du socket Client
	client.connect(("127.0.0.1",55000)) #connecter le client au serveur en passant par le port 42000
	
	client1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client1.bind(("127.0.0.1",55001)) # creation d'interface de communication en passant par le port 550000

	while "true":
		print ("\n------------------------------------------------")
		print ("Tapez 1 -->  POUR AVOIR LES DETAILS SUR UN LIVRE")
		print ("Tapez 2 -->  POUR LISTER TOUS LES LIVRE")
		print ("------------------------------------------------")
		choix = input("Votre choix: ")
		print ("------------------------------------------------")

		if choix == "1" : 
			
			idlivre = input("Veuillez saisir l identifiant du livre: ")
			print ("\n\n")
			data = str(choix) + ";" + str(idlivre)
			client.send(bytes(data.encode()))
			
			client1.listen(1) # limite le nombre requettes a 2 seulement
			serveur1, infos = client1.accept() # accept et attend la connexion du client
			msg = serveur1.recv(1024)
			data = pickle.loads(msg)
			print ("----------------------------")
			for row in data:
				
				print (row[0][0], "--->", row[1])
			print ("----------------------------")
			
		elif choix == "2" :
			
			client.send(bytes(choix.encode()))
			
			client1.listen(1) # limite le nombre requettes a 2 seulement
			serveur1, infos = client1.accept() # accept et attend la connexion du client
			find=True
			while 1:
				msg = serveur1.recv(1024)
				
				if msg != 0 :
					data = pickle.loads(msg)
		
					for row in data:									
						print ("--->", row)
						print ("----------------------------")
		else :
			
			print("rien")
		
client()