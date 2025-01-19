import os
FILE_NAME = "contacts.txt"


def add_contact():
    """Функція для додавання нового контакту."""
    name = input("Введіть ім'я: ")
    phone = input("Введіть номер телефону: ")
    email = input("Введіть електронну пошту: ")


    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'w') as file:
            pass


    with open(FILE_NAME, 'a') as file:
        file.write(f"Ім'я: {name}, Телефон: {phone}, Електронна пошта: {email}\n")
    print("Контакт успішно додано!")


def view_contacts():
    """Функція для перегляду всіх контактів."""
    if not os.path.exists(FILE_NAME):
        print("Файл з контактами ще не створено.")
        return


    with open(FILE_NAME, 'r') as file:
        contacts = file.readlines()
        if contacts:
            print("Список контактів:")
            for contact in contacts:
                print(contact.strip())
        else:
            print("Файл з контактами порожній.")


def main():
    """Основна функція програми."""
    while True:
        print("\nМеню:")
        print("1. Додати новий контакт")
        print("2. Переглянути список контактів")
        print("3. Вийти")


        choice = input("Виберіть дію (1/2/3): ")
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            print("Програма завершила роботу.")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")


if __name__ == "__main__":
    main()
   
