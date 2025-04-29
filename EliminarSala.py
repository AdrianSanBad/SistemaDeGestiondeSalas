# import the sql library to connect to the database
import mysql.connector

# delete the sala with the id passed as parameter  checking if the sala is available (disponible==True)
def eliminarSala(id_sala,disponible):
    #if the sala is available (disponible==True) then change the state of estado to false 
    if disponible:
        # connect to the database
        connection = mysql.connector.connect(host='localhost',
                                             database='Gestion_Salas',
                                             user="root",
                                                password='1234qwer#')
        cursor = connection.cursor()
        # update the estado of the sala to false (eliminada)
        consulta = "UPDATE salas SET estado = 0 WHERE id_sala = %s"
        cursor.execute(consulta, (id_sala,))
        # commit the changes to the database
        connection.commit()
        cursor.close()
        connection.close()
        print("La sala ha sido eliminada correctamente")
    else:
        print("La sala no se puede eliminar porque tiene reservas activas")
        return False
    return True
eliminarSala(1,True)