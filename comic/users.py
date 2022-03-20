from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

def get_db():
    try:
        print("conexion exitosa")
        client = MongoClient("mongodb+srv://esbeydy:esbeydy@esbeydy.jj8dd.mongodb.net/usersDB?retryWrites=true&w=majority")
        db = client.usersDB
        
    except ConnectionFailure:
        print("Error de conexion")
    return db

def consultar_datos(email,password):
    try:
        db = get_db()
        usuarios= db.usuarios.find({"email":email,"password":password})
        """
        print("{:<50} {:20} {:20} {:20} {:10}".format("name","email", "age","password","token"))
        for user in users:
            print("{:<50} {:<20} {:<20} {:<20} {:,.2f}".format(users["name"], users["email"], users["age"], users["password"], users["token"]))
        """    
        print(usuarios["name"], usuarios["email"], usuarios["age"], usuarios["password"], usuarios["token"])
    except:
        print("ocurrio un error al obtener la información")
    return usuarios

def regitro_user():
    try:
        db = get_db()
        new_user ={
        "name": 'Badra Vargas',
        "email": 'badrav@gamil.com',
        "age": 22,
        "password": 'qwert',
        "token": 'mi token'
        }
        registro = db.usarios.insert_one(new_user)
    except:
        print("ocurrio un error al registrar usuario")
    return registro


#Menu
print("sistema de control de usuarios")
while(True):
    print("1.-Iniciar sesión")
    print("2.-Registrarme")
    print("3.-Consultar mis datos")
    print("4.-Salir")
       
    filter = input("Elige una opcion:")

    if filter == '1':
        print("> Iniciar sesión")
        
    elif filter == '2':
        print("> Registrate")
        regitro_user()
    elif filter == '3':
        print("> Consulta tus datos")

        email = input("ingresa tu email:")
        password = input("ingresa tu password:")
        consultar_datos(email,password)
    elif filter == '4':
        break
    else:
        print("opcion desconocida, vuelve a intentarlo")




      