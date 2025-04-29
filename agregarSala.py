# import the sql library to connect to the database
import mysql.connector
#insert a new Sala
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
        #insert create a row in the table salas
        sql_delete_query = """INSERT INTO salas(nombre, capacidad, estado)  VALUES (%s, %s, %s)"""
        val = (nombreSala, capacidad, 1)
        cursor.execute(sql_delete_query, val)
        # commit the changes to the database
        connection.commit()
        print("Sala agregada con exito")
    except mysql.connector.Error as error:
        print("Error al agregar la sala: {}".format(error))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión a MySQL cerrada")
agregarSala()
