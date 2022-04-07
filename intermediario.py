#------------------------intermediario.py-----------------------------
#TODO: Hacer que verifique disponibilidad con el servidor gato (El codigo de la linea 35 es temporal)
#TODO: Saber si hay ganadores revisando el tablero e informar al jugador en el caso de que haya
#TODO: No se que mas
#---------------------------------------------------------------

import socket as skt

#Direccion IP(IPv4) y puerto para comunicarse con el cliente y el servidor gato
direccion = 'localhost'
puertoCliente = 5002
puertoGato = 7000

#conexion del socket cliente-intermediario
socketIntermediario = skt.socket(skt.AF_INET, skt.SOCK_STREAM) #IPv4, TCP
socketIntermediario.bind((direccion, puertoCliente))
socketIntermediario.listen(1)

print("Esperando conexion del cliente")
socketCliente, direccionCliente = socketIntermediario.accept() #Espera a que el cliente se conecte
print("Conectado a: {}".format(direccionCliente))

while True:

    print("Esperando opcion escogida por el cliente")
    opcion = socketCliente.recv(1024).decode()

    print("Opcion escogida: {}".format(opcion))

    if(opcion == "1"):

        #Inicializacion del socket intermediario-gato
        socketGato = skt.socket(skt.AF_INET, skt.SOCK_DGRAM) #IPv4, UDP
        
        disponibilidad = "OK" #Temporal
        socketCliente.send(disponibilidad.encode())

        if(disponibilidad=="OK"):

            status = "playing"

            while(status == "playing"):

                tablero = socketCliente.recv(1024).decode()

                print("Estado: {}".format(status))
                print(tablero)
        
        socketGato.close()
    else:
        break

print("Cerrando servidor intermediario")
socketCliente.close()
