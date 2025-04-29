#import the librarie to use sql
import mysql.connector
# use a select to view the sala with the id passed as parameter and check if estado is 1
def consultarSala(id_sala):
    # connect to the database
    connection = mysql.connector.connect(host='localhost',
                                         database='Gestion_Salas',
                                         user='root',
                                         password='1234qwer#')
    cursor = connection.cursor()
    # select the sala with the id passed as parameter and check if estado is 1
    consulta = "SELECT * FROM salas WHERE id_sala = %s AND estado = 1"
    cursor.execute(consulta, (id_sala,))
    # fetch the result of the query
    result = cursor.fetchone()
    # if the result is not empty then the sala is available (disponible==True)
    if result:
        print("La sala con id {} es: {}".format(id_sala, result))
        return True
    else:
        print("La sala con id {} no existe o no está disponible".format(id_sala))
        return False
    # close the connection to the database
    cursor.close()
    connection.close()
#Prueba de la funcion consultarSala 
# consultarSala(1) 
# esta sala no existe
   
#consultarSala(2)
# esta sala existe y esta disponible mostrando los datos de la sala