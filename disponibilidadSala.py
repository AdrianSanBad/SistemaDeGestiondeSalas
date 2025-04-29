# import the sql library to connect to the database
import mysql.connector
# mediante una consulta sql se revisa la disponibilidad de la sala con el id pasado como parametro en los horarios del dia en la fecha dada
def disponibilidadSala(id, fecha):
    # connect to the database
    connection = mysql.connector.connect(host='localhost',
                                         database='sala',
                                         user='root',
                                         password='1234pwc')
    cursor = connection.cursor()
    # check if the sala is available (disponible==True) in the date passed as parameter filtring by the id of the sala and one join with the reserva table
    sql