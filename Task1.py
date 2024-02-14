import random
import string

def generate_password(length, use_uppercase, use_digits, use_special_chars):
    chars = string.ascii_lowercase
    if use_uppercase:
        chars += string.ascii_uppercase
    if use_digits:
        chars += string.digits
    if use_special_chars:
        chars += string.punctuation

    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def main():
    length = int(input("Введіть довжину паролю: "))
    use_uppercase = input("Використовувати великі літери? (Так/Ні): ").lower() == 'так'
    use_digits = input("Використовувати цифри? (Так/Ні): ").lower() == 'так'
    use_special_chars = input("Використовувати спеціальні знаки? (Так/Ні): ").lower() == 'так'

    password = generate_password(length, use_uppercase, use_digits, use_special_chars)
    print("Згенерований пароль:", password)

if __name__ == "__main__":
    main()

