
# Projet personnel d’Adam — candidature IUT Informatique

import random
import string

def caesar_shift(text, shift):
    """Décale les lettres selon la méthode César"""
    result = ""
    for c in text:
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            result += chr((ord(c) - base + shift) % 26 + base)
        else:
            result += c
    return result

def random_letters(n):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(n))

def random_numbers(n):
    return ''.join(random.choice(string.digits) for _ in range(n))

def random_specials(n):
    specials = "!@#$%^&*()-_=+[]{};:,.?/<>"
    return ''.join(random.choice(specials) for _ in range(n))

def generate_password(length=12, shift=3, letters=6, numbers=3, specials=3):
    if letters + numbers + specials != length:
        raise ValueError("letters + numbers + specials doivent = longueur totale")
    l = random_letters(letters)
    l_shifted = caesar_shift(l, shift)
    n = random_numbers(numbers)
    s = random_specials(specials)
    pwd_list = list(l_shifted + n + s)
    random.shuffle(pwd_list)
    return ''.join(pwd_list)

if __name__ == "__main__":
    pwd = generate_password()
    print("Mot de passe généré :", pwd)
