from fabulous.color import red, green, cyan, yellow

# Funciones del menú


def show_contacts(phone_book):
    if phone_book == {}:
        print(red("No hay contactos en Phone_book"))
    else:
        for name, phone in phone_book.items():
            print(cyan(name, ":", phone))


def add_contact(phone_book, name, phone):

        phone_book[name] = phone


def remove_contact(phone_book, name):

    if name in phone_book:
        del(phone_book[name])
    else:
        print(red("ERROR: este contacto no existe"))


def menu():
    phone_book = {}

    while True:
        print(yellow("\n1-Mostrar lista de contactos"))
        print(yellow("2-Añadir contacto (nombre y teléfono)"))
        print(yellow("3-Borrar contacto (nombre)"))
        print(yellow("4-Salir\n"))

        menu = input("¿Menú a elegir?: ")

        if menu == "1":
            show_contacts(phone_book)
        elif menu == "2":
            name = input(green("¿Contacto que desea añadir?: "))
            if name not in phone_book:
                phone = input(green("¿Número de contacto?: "))
                add_contact(phone_book, name, phone)
            else:
                print(red("ERROR: este contacto ya existe"))
        elif menu == "3":
            name = input(green("¿Contacto que desea eliminar?: "))
            remove_contact(phone_book, name)
        elif menu == "4":
            break
        else:
            print(red("ERROR: menú incorrecto!!"))

# Ejecución

menu()
