import random
import string
import json

MAPPING_FILE = 'random_mapping.json'


def generate_random_mapping():
    alphabet = list(string.printable)
    random_mapping = {letter: ''.join(random.choices(string.ascii_lowercase, k=8)) for letter in alphabet}

    # Save the mapping to a file
    with open(MAPPING_FILE, 'w') as file:
        json.dump(random_mapping, file)

    return random_mapping


def load_mapping_from_file():
    try:
        with open(MAPPING_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return None


def encrypt_sentence(sentence, mapping):
    encrypted_sentence = ''.join([mapping.get(char, char) for char in sentence.lower()])
    return encrypted_sentence


def main():
    existing_mapping = load_mapping_from_file()

    if existing_mapping:
        print("Mapping déja écrit :")
        for letter, value in existing_mapping.items():
            print(f"{letter}: {value}")
    else:
        existing_mapping = generate_random_mapping()
        print("Nouveau mapping généré :")

    sentence = input("Écrivez votre phrase : ")

    encrypted_sentence = encrypt_sentence(sentence, existing_mapping)

    print(f"Phrase encryptée : {encrypted_sentence}")


if __name__ == "__main__":
    main()