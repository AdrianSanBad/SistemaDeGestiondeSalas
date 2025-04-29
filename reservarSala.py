# import the sql library to connect to the database
import mysql.connector
#reserv sala
def reservarSala():
    # connect to the database
    connection = mysql.connector.connect(host='localhost',
                                            database='Gestion_Salas',
                                            user="root",
                                            password='1234qwer#')
    
    usuario = int(input("Usuario: "))
    sala = int(input("Sala: "))
    hInicio = int(input("Fecha y hora de Inicio: "))
    hFin = int(input("Fecha y hora de Fin: "))
    
    sql_select_query = """SELECT estado FROM salas WHERE  nombre = %s"""
    disponible = cursor.execute(sql_select_query, sala)
    
    sql_select_query = """SELECT id_sala FROM salas WHERE  nombre = %s"""
    idSala = cursor.execute(sql_select_query, sala)

    sql_select_query = """SELECT id_usuario FROM usuarios WHERE  nombre = %s"""
    idUsuario = cursor.execute(sql_select_query, usuario)
    #if the sala is available (disponible==True) then change the state of estado to false 
    if disponible:
        cursor = connection.cursor()
        # use the data that the user give
        val = (idSala, idUsuario, hInicio, sala)

        sql_delete_query = """INSERT INTO reserva(id_sala, id_usuario, inicio, fin)  VALUES (%s, %s,%s, %s) wh"""
        cursor.execute(consulta, val)

        connection.commit()
        cursor.close()
        connection.close()
        print("La sala ha sido eliminada correctamente")
    else:
        print("La sala no se puede eliminar porque tiene reservas activas")
        return False
    return True


reservarSala()