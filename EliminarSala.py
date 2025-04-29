# import the sql library to connect to the database
import mysql.connector
# delete the sala with the id passed as parameter  checking if the sala is available (disponible==True)
def eliminarSala(id,disponible):
    #if the sala is available (disponible==True) then delete the sala from the database
    if disponible is True:
        try:
            # connect to the database
            connection = mysql.connector.connect(host='localhost',
                                                 database='sala', 
                                                 user='root',
                                                 password='1234pwc')
            cursor = connection.cursor()
            # delete the sala with the id passed as parameter
            sql_delete_query = """DELETE FROM sala WHERE id = %s"""
            cursor.execute(sql_delete_query, (id,))
            # commit the changes to the database
            connection.commit()
            print("Sala eliminada con exito")
        #if the sala is not available (disponible==False) then print a message
        except mysql.connector.Error as error:
            print("Error al eliminar la sala: {}".format(error))
        #the conection to the database is closed after the operation is done
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("Conexión a MySQL cerrada")