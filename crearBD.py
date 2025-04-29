import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234pwc"
)

mycursor = mydb.cursor()

def crearBD():
    mycursor.execute("CREATE DATABASE IF NOT EXISTS Gestion_Salas")
    mycursor.execute("USE Gestion_Salas")
    mycursor.execute("CREATE TABLE salas (id_sala INTEGER PRIMARY KEY AUTO_SUMARY, nombre VARCHAR(6) CHECK(nombre LIKE 'Sala %', capacidad INTEGER))")
    mycursor.execute("CREATE TABLE reserva (id_sala INTEGER, id_usuario INTEGER, inicio DATETIME , fin DATETIME, activa BOOLEAN,PRIMARY KEY(id_reserva,id_usuario)")
    mycursor.execute("CREATE TABLE usuarios(id_usuario INTEGER PRIMARY KEY AUTO_SUMARY, nombre VARCHAR(50), contraseña VARCHAR(16))")