import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234qwr#"
)

mycursor = mydb.cursor()

def crearBD():
    mycursor.execute("CREATE DATABASE IF NOT EXISTS Gestion_Salas")
    mycursor.execute("USE Gestion_Salas")
    mycursor.execute("CREATE TABLE salas (id_sala INTEGER PRIMARY KEY AUTO_INCREMENT, nombre VARCHAR(6) CHECK(nombre LIKE 'Sala %'), capacidad INTEGER, estado BOOLEAN)")
    mycursor.execute("CREATE TABLE usuarios(id_usuario INTEGER PRIMARY KEY AUTO_INCREMENT, nombre VARCHAR(50), contraseña VARCHAR(16))")
    mycursor.execute("CREATE TABLE reserva (id_sala INTEGER, id_usuario INTEGER, inicio DATETIME, fin DATETIME, activa BOOLEAN,PRIMARY KEY(id_sala,id_usuario), FOREIGN KEY (id_sala) REFERENCES salas(id_sala), FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario))")
   