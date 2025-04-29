# import the sql library to connect to the database
import mysql.connector
def agregarSala():
    
        try:
            # connect to the database
            connection = mysql.connector.connect(host='localhost',
                                                 database='Gestion_Salas', 
                                                 user='root',
                                                 password='1234qwer#')
            cursor = connection.cursor()
            nombreSala = input("Nombre de la sala: ")
            capacidad = int(input("Capacidad de la sala: "))
            #
            sql_delete_query = """INSERT INTO salas(nombre, capacidad, estado)  VALUES (%s, %s, %s)"""
            val = (nombreSala, capacidad, 1)
            cursor.execute(sql_delete_query, val)
            # commit the changes to the database
            connection.commit()
            print("Sala agregada con exito")
        #if the sala is not available (disponible==False) then print a message
        except mysql.connector.Error as error:
            print("Error al agregar la sala: {}".format(error))
        #the conection to the database is closed after the operation is done
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("Conexión a MySQL cerrada")
agregarSala()
