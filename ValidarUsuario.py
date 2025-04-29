import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234pwc"
)

mycursor = mydb.cursor()

def getUser():
    usuario = input("Ingresa el Nombre de usuario")
    password = getpass.getpass('Password:')
    mycursor.execute("SELECT * FROM usuarios")
    myresult = mycursor.fetchall()
    for x in myresult:
        if x == usuario:
            passwordbase= "SELECT contraseña FROM usuarios WHERE usuario LIKE '%s' "
            mycursor.execute(passwordbase,usuario)
            for y in myresult:
                if y == password:
                    print("Usuario Validado")


    




if __name__ == "__main__":
    getUser()