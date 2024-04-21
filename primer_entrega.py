# <<< CLASE 10 - Primer Entrega Trabajo Final

# <<< Objetivo
# Practicar el concepto de funciones. Preparar la parte lógica para el registro de usuarios.

# <<< Consigna
# Crear un programa que permita emular el registro y almacenamiento de usuarios en una base de datos.
# Crear el programa utilizando el concepto de funciones, diccionarios, bucles y condicionales.

# <<< Formato
# El proyecto debe compartirse utilizando Colab bajo el nombre “Primera pre-entrega+Apellido”.

# <<< Se debe entregar
# Se debe entregar todo el programa.

# <<< Sugerencias
# El formato de registro es: Nombre de usuario y Contraseña.
# Utilizar una función para almacenar la información y otra función para mostrar la información.
# Utilizar un diccionario para almacenar dicha información, con el par usuario-contraseña (clave-valor).
# Utilizar otra función para el login de usuarios, comprobando que la contraseña coincida con el usuario.

# <<< Adicional
# Utilizando los conceptos de la clase 8, guarde la información en un archivo de texto dentro de su Drive."

import json


# <<< Cargar la base de datos desde el archivo
def cargar_db():
    try:
        with open("db.txt", "r") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return {}  # Retorna un diccionario vacío si el archivo no existe


# <<< Guardar la base de datos en txt
def guardar_db(db):
    with open("db.txt", "w") as archivo:
        json.dump(db, archivo)


# TEST: Cargar la base de datos desde el archivo
db = cargar_db()


# <<< Crear nuevo usuario - Utilizar una función para almacenar la información y otra función para mostrar la información
def new_user(db, usuario, clave):
    # TODO incorporar una librería para generar users automáticos con UID
    user_count = len(db) + 1  # Sumar uno para el nuevo usuario
    new_user_id = f"user{user_count}"

    # Añadir el nuevo usuario al diccionario
    db[new_user_id] = {"username": usuario, "password": clave}
    guardar_db(db)  # Guardar los cambios en el txt
    return new_user_id  # Retorna el ID del nuevo usuario


# TEST: Añadir un nuevo usuario
username_buscado = input("Crear nuevo usuario => Ingrese un nombre de usuario: ")
password_buscado = input("Crear nuevo usuario => Ingrese una contraseña: ")
usuario_id = new_user(db, username_buscado, password_buscado)
print(f"El ID del usuario creado es: {usuario_id}")


# <<< Encontrar user buscando por username y password
def encontrar_usuario_por_username(db, username_buscado, password_buscado):
    for user_id, user_info in db.items():
        if (
            user_info["username"] == username_buscado
            and user_info["password"] == password_buscado
        ):
            return user_id  # Retorna el ID del usuario
    return None  # Retorna None si no se encuentra el usuario


# TEST: Encontrar un usuario existente
username_buscado = input("Login usuario: Ingrese su nombre de usuario para verificar: ")
password_buscado = input("Login usuario: Ingrese su contraseña para verificar: ")
usuario_id = encontrar_usuario_por_username(db, username_buscado, password_buscado)


# <<< Mostrar los primeros 5 users
def mostrar_primeros_cinco_usuarios(db):
    contador = 0
    print("Usuarios cargados en la db: ")
    for user_id, user_info in db.items():
        print(
            f"ID: {user_id}, Username: {user_info['username']}, Password: {user_info['password']}"
        )
        contador += 1
        if contador == 5:
            break


# TEST: Mostrar los primeros 5 users
mostrar_primeros_cinco_usuarios(db)

if usuario_id:
    print(f"El ID del usuario es: {usuario_id}")
else:
    print(f"Usuario {username_buscado} no encontrado")

##<<< Expandir funcionalidades
# Eliminar usuario
######## del db['user2']

# Acceder al nombre de usuario de user1
######## username_user1 = db['user1']['username']

# Cambiar la contraseña de user1
######## db['user1']['password'] = 'newpass123'

##<<< Base de datos ejemplo forma
# db = {
#    'user1': {
#        'username': 'ferjen',
#        'password': '123456'
#    },
#    'user2': {
#        'username': 'lionelmess',
#        'password': '123456'
#    }
# }
