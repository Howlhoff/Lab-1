#------------------------cliente.py-----------------------------
#TODO: Revisar que coordJugada(Linea 37) tenga el formato correcto
#TODO: Revisar que las coordenadas escogidas por el jugador no sean de una casilla ocupada
#TODO: No se que mas
#---------------------------------------------------------------

import socket as skt

#Direccion IP(IPv4) y puerto para comunicarse con el servidor
direccion = 'localhost'
puerto = 5002

#Inicializacion del socket cliente-servidor1
socketCliente = skt.socket(skt.AF_INET, skt.SOCK_STREAM) #IPv4, TCP
socketCliente.connect((direccion, puerto))

while(True):
    print("-------- Bienvenido al Juego --------\n -Seleccione una opcion\n  1) Jugar\n  2) Salir")

    opcion = input("Ingrese una opcion: ")

    if(opcion == "1"):

        socketCliente.send(opcion.encode())                  #Avisa al servidor sobre el inicio de una partida
        disponibilidad = socketCliente.recv(1024).decode()   #Recibe el mensaje sobre la disponibilidad

        print("Respuesta de disponibilidad: {}".format(disponibilidad))

        if(disponibilidad == "OK"):

            status = "playing"  #Estado del juego
            tableroGato = "\n  │ 0 │ 1 │ 2 │\n───┼───┼───┼───┤\n 0 │   │   │   │\n───┼───┼───┼───┤\n 1 │   │   │   │\n───┼───┼───┼───┤\n 2 │   │   │   │\n───┴───┴───┴───┘"

            while(status == "playing"):
                print(tableroGato)

                coordJugada = input("Ingrese su jugada (x,y): ")

                index = 39  + (4*int(coordJugada[1])) + (34*int(coordJugada[3])) # Formula para ingresar los simbolos en el tablero: OffsetPrimeraCasilla + (Offset_X*coord_X) + (Offset_Y*coord_Y)
                tableroGato = tableroGato[:index] + "o" + tableroGato[index+1:]

                socketCliente.send(tableroGato.encode())

                status = socketCliente.recv(1024).decode()
                tableroGato = socketCliente.recv(1024).decode()
            
            if(status == "Won"):
                print("Ganaste la partida")
            else:
                print("Perdiste")

    elif(opcion == "2"):
        socketCliente.send(opcion.encode())
        break
    else:
        print("Opcion invalida")

print("Saliendo del Juego")
socketCliente.close()
