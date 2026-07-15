from cryptography.fernet import Fernet

# Run this ONLY ONCE to generate the key file,
# then comment it again.


def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

write_key()

# Master Password
master_pwd = input("What is the master password? ")

if master_pwd != "12345":      # Change this to your own password
    print("Incorrect master password!")
    quit()


def load_key():
    with open("key.key", "rb") as file:
        key = file.read()
    return key


key = load_key()
fer = Fernet(key)


def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()

            if "|" not in data:
                continue

            user, passw = data.split("|")
            print(
                "User:", user,
                "| Password:", fer.decrypt(passw.encode()).decode()
            )


def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open("passwords.txt", "a") as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")


while True:
    mode = input(
        "\nWould you like to add a new password or view existing ones?\n"
        "(view/add) or press q to quit: "
    ).lower()

    if mode == "q":
        break

    elif mode == "view":
        view()

    elif mode == "add":
        add()

    else:
        print("Invalid mode.")

print("Goodbye!")