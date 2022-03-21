from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

#Aqui se hace la configuración para la conexión de la base de datos
def get_db():
    try:
        #client = MongoClient("mongodb://esbeydy:esbeydy@esbeydy-shard-00-00.jj8dd.mongodb.net:27017,esbeydy-shard-00-01.jj8dd.mongodb.net:27017,esbeydy-shard-00-02.jj8dd.mongodb.net:27017/usersDB?ssl=true&replicaSet=atlas-u98ok0-shard-0&authSource=admin&retryWrites=true&w=majority")
        #client = MongoClient("mongodb+srv://esbeydy:esbeydy@Esbeydy.jj8dd.mongodb.net/usersDB?retryWrites=true&w=majority")
        #db = client.usersDB
        client = MongoClient('mongodb+srv://esbeydy:7697@esbeydy.jj8dd.mongodb.net/usersDB?retryWrites=true&w=majority',tls=True,tlsAllowInvalidCertificates=True)
        mydb = client["usersDB"]
        mycol = mydb["usuarios"]
        print("conexion exitosa")
    except ConnectionFailure:
        print("Error de conexion")
    return mycol

#Función para consultar datos de usuario, ingresando email y contraseña
def consultar_datos(email,password):
    try:
        db = get_db()
        #usuarios= db.usuarios.find({"email":email,"password":password})
        usuario = list(db.find({"email":email,"password":password})) 
        print(usuario)

    except Exception as e:
        print("ocurrio un error al obtener la información")
        print(e)
    return True
    
#Función para registro de usuario
def regitro_user(name,email,age,password,token):
    try:
        db = get_db()
        
        new_user ={name,email,age,password,token}
        registro = db.insert_one(new_user)
        #print (registro)
    except Exception as e:
        print("ocurrio un error al registrar usuario")
        print(e)
    return registro

#Inicio de sesión
def longin(email,password):
    try:
        db = get_db()
        if db.mycol.email == email  and db.mycol.password == password:
            print("Bienvenido")
        else:
            print("Datos incorrectos")
    except Exception as e:
        print(e)
    return True

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
        email = input("ingresa tu email:")
        password = input("ingresa tu password:")
        longin(email,password)
        
    elif filter == '2':
        print("> Registrate")
        name = input("Ingresa tu nombre completo:")
        email = input("Ingresa tu email:")
        age = input("Ingresa tu edad:")
        password = input("Ingresa tu contraseña:")
        token = input("Ingresa tu token:")
        regitro_user(name,email,age,password,token)
    elif filter == '3':
        print("> Consulta tus datos")
        email = input("ingresa tu email:")
        password = input("ingresa tu password:")
        consultar_datos(email,password)
    elif filter == '4':
        break
    else:
        print("opcion desconocida, vuelve a intentarlo")




      