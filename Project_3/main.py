import secrets
import string

def generate_password(length):
    characters = (
        string.ascii_letters +
        string.digits
    )

    password = ''.join(
        secrets.choice(characters)
        for _ in range(length)
    )

    return password

def main():
    print("-------RANDOM PASSWORD GENERATOR-------")

    while True:
        try:
            length = int(input("Enter password length: "))

            if length <= 0:
                print("Password length must be greater than 0.\n")
                continue

            password = generate_password(length)

            print("\nGenerated Password:")
            print(password)

            break

        except ValueError:
            print("Please enter a valid integer.\n")


if __name__ == "__main__":
    main()