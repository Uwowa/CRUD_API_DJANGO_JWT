import os
import django
import requests

# Configuración de Django para usar el modelo fuera del entorno web
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'poo.settings')
django.setup()

from programadores.models import Programmer

def authenticate():
    print("=== Autenticación JWT ===")
    url = "http://localhost:8000/api/token/"
    username = input("Nombre de usuario: ")
    password = input("Contraseña: ")
    response = requests.post(url, data={"username": username, "password": password})
    if response.status_code == 200:
        tokens = response.json()
        print("Autenticación exitosa.")
        return tokens['access']
    else:
        print("Error de autenticación.")
        return None

def show_menu():
    print("\n=== Menú CRUD para Programadores ===")
    print("1. Listar programadores")
    print("2. Crear un programador")
    print("3. Actualizar un programador")
    print("4. Eliminar un programador")
    print("5. Salir")

def list_programmers(token):
    url = "http://localhost:8000/api/Programadores/"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        programmers = response.json()
        if programmers:
            for p in programmers:
                print(f"ID: {p['id']} | Nombre: {p['nombre']} | Apellidos: {p['apellidos']} | Email: {p['email']} | Username: {p['username']} | Edad: {p['edad']} | Activo: {p['is_active']}")
        else:
            print("No hay programadores registrados.")
    else:
        print("Error al listar programadores.")

def create_programmer(token):
    url = "http://localhost:8000/api/Programadores/"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "nombre": input("Nombre: "),
        "apellidos": input("Apellidos: "),
        "email": input("Email: "),
        "username": input("Username: "),
        "edad": int(input("Edad: ")),
        "is_active": input("¿Está activo? (s/n): ").lower() == 's'
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 201:
        print("Programador creado exitosamente.")
    else:
        print("Error al crear programador.")

def update_programmer(token):
    id = input("ID del programador a actualizar: ")
    url = f"http://localhost:8000/api/Programadores/{id}/"
    headers = {"Authorization": f"Bearer {token}"}
    data = {}
    nombre = input("Nombre: ")
    if nombre:
        data['nombre'] = nombre
    apellidos = input("Apellidos: ")
    if apellidos:
        data['apellidos'] = apellidos
    username = input("Username: ")
    if username:
        data['username'] = username
    email = input("Email: ")
    if email:
        data['email'] = email
    edad = input("Edad: ")
    if edad:
        data['edad'] = int(edad)
    is_active = input("¿Está activo? (s/n): ")
    if is_active:
        data['is_active'] = is_active.lower() == 's'

    response = requests.put(url, headers=headers, json=data)
    if response.status_code == 200:
        print("Programador actualizado exitosamente.")
    else:
        print("Error al actualizar programador.")

def delete_programmer(token):
    id = input("ID del programador a eliminar: ")
    url = f"http://localhost:8000/api/Programadores/{id}/"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.delete(url, headers=headers)
    if response.status_code == 204:
        print("Programador eliminado exitosamente.")
    else:
        print("Error al eliminar programador.")

def main():
    token = authenticate()
    if not token:
        print("No se puede continuar sin autenticación.")
        return

    while True:
        show_menu()
        choice = input("Seleccione una opción: ")
        if choice == '1':
            list_programmers(token)
        elif choice == '2':
            create_programmer(token)
        elif choice == '3':
            update_programmer(token)
        elif choice == '4':
            delete_programmer(token)
        elif choice == '5':
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()
